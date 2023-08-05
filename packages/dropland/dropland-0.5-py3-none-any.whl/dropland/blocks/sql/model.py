import contextlib
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Set, Tuple, TypeVar, Union

from dependency_injector.wiring import Provide
from pydantic.main import BaseModel as PydanticModel
from sqlalchemy import Column, exists, func, literal_column, select, tuple_
from sqlalchemy.sql import ColumnCollection

from dropland.data.context import ContextData, get_context
from dropland.storages.base import StorageModel as BaseModel
from .engine import SqlStorageEngine, SqlStorageType

CreateSchemaType = TypeVar('CreateSchemaType', bound=PydanticModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=PydanticModel)


class SqlTableInfo(NamedTuple):
    db_type: SqlStorageType
    backend: str
    is_async: bool


class SqlModelBase(BaseModel):
    _sql_engine = None

    # noinspection PyUnresolvedReferences
    @classmethod
    def _check_abstract(cls):
        if cls.__table__ is None:
            raise TypeError(f'Model {cls.__name__} is abstract, no table is defined!')

    def __eq__(self, other: 'SqlModelBase'):
        self._check_abstract()
        return type(self) == type(other) and self.get_id_value() == other.get_id_value()

    def __hash__(self):
        self._check_abstract()
        return self.get_id_value().__hash__()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.Meta.private_fields.update({'metadata', 'registry'})
        cls.Meta.non_serializable_fields.update({'metadata', 'registry'})

    def get_id_value(self) -> Any:
        return self._get_column_values(self._get_id_columns())

    @classmethod
    def get_engine(cls) -> SqlStorageEngine:
        return cls._sql_engine

    @classmethod
    def get_table_info(cls) -> SqlTableInfo:
        engine = cls.get_engine()
        return SqlTableInfo(db_type=engine.db_type, backend=engine.backend.name, is_async=engine.is_async)

    @classmethod
    @contextlib.contextmanager
    def _connection_context(
            cls, begin_tx: bool = False, autocommit: bool = False, session=Provide['session']):
        info, ctx = cls.get_table_info(), get_context()
        assert not info.is_async, 'Use async_connection_context() function instead'
        if hasattr(ctx, 'sql'):
            yield ctx
        else:
            with session.connection_context(info.db_type, info.backend, begin_tx, autocommit) as c:
                ctx.sql = c
                yield ctx
                del ctx.sql

    @classmethod
    @contextlib.asynccontextmanager
    async def _async_connection_context(
            cls, begin_tx: bool = False, autocommit: bool = False, async_session=Provide['async_session']):
        info, ctx = cls.get_table_info(), get_context()
        assert info.is_async, 'Use connection_context() function instead'
        if hasattr(ctx, 'sql'):
            yield ctx
        else:
            session = await async_session
            async with session.async_connection_context(info.db_type, info.backend, begin_tx, autocommit) as c:
                ctx.sql = c
                yield ctx
                del ctx.sql

    @classmethod
    def query_for_select(cls, **kwargs):
        raise NotImplementedError

    @classmethod
    def query_for_update(cls, **kwargs):
        raise NotImplementedError

    @classmethod
    def query_for_delete(cls, **kwargs):
        raise NotImplementedError

    # noinspection PyUnresolvedReferences
    @classmethod
    def get_columns(cls) -> ColumnCollection:
        return cls.__table__.columns

    #
    # Retrieve operations
    #

    @classmethod
    async def get(cls, id_value: Any, **kwargs) -> Optional['SqlModelBase']:
        async with cls._async_connection_context() as ctx:
            if instance := cls._get_from_local_cache(ctx, [id_value])[0]:
                return instance
            query = cls.query_get(id_value, **kwargs)
            if instance := await cls.perform_get(ctx, query, **kwargs):
                await cls._register_instances(ctx, [instance])
                return await cls._build_rela(ctx, instance, **kwargs)
        return None

    @classmethod
    async def list(cls,
                   filters: Optional[List[Any]] = None,
                   sorting: Optional[List[Any]] = None,
                   skip: int = 0, limit: int = 0, params: Dict[str, Any] = None, **kwargs) -> List['SqlModelBase']:
        query = cls.query_list(filters or [], sorting or [], skip, limit, params, **kwargs)
        async with cls._async_connection_context() as ctx:
            if objects := await cls.perform_list(ctx, query, **kwargs):
                await cls._register_instances(ctx, objects)
                return await cls._build_rela_list(ctx, objects, **kwargs)
            return []

    @classmethod
    async def get_any(cls, indices: List[Any], **kwargs) -> List[Optional['SqlModelBase']]:
        async with cls._async_connection_context() as ctx:
            objects = cls._get_from_local_cache(ctx, indices)
            non_cached_indices = [i for o, i in zip(objects, indices) if o is None]
            if non_cached_indices:
                query = cls.query_any(non_cached_indices, **kwargs)
                if non_cached := await cls.perform_any(ctx, query, **kwargs):
                    await cls._register_instances(ctx, non_cached)
                    objects += await cls._build_rela_list(ctx, non_cached, **kwargs)

        objects = {obj.get_id_value(): obj for obj in objects if obj is not None}
        return [objects[id_value] if id_value in objects else None for id_value in indices]

    @classmethod
    async def count(cls, filters: Optional[List[Any]] = None, params: Dict[str, Any] = None, **kwargs) -> int:
        query = cls.query_count(filters, params, **kwargs)
        async with cls._async_connection_context() as ctx:
            return await cls.perform_count(ctx, query, **kwargs)

    @classmethod
    async def exists(cls, id_value: Any, **kwargs) -> bool:
        async with cls._async_connection_context() as ctx:
            if cls._has_in_local_cache(ctx, [id_value])[0]:
                return True
            query = cls.query_exists(id_value, **kwargs)
            return await cls.perform_exists(ctx, query, **kwargs)

    @classmethod
    async def exists_by(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs) -> bool:
        if not filters or not isinstance(filters, list):
            return False

        query = cls.query_exists_by(filters, params, **kwargs)
        async with cls._async_connection_context() as ctx:
            return await cls.perform_exists_by(ctx, query, **kwargs)

    #
    # Modification operations
    #

    @classmethod
    async def create(cls, data: Union[CreateSchemaType, Dict[str, Any]], **kwargs) -> Optional['SqlModelBase']:
        if isinstance(data, dict):
            create_data = data
        else:
            create_data = data.dict(exclude_unset=True)

        if create_data:
            create_data = cls.prepare_for_create(create_data)

        async with cls._async_connection_context(begin_tx=True, autocommit=True) as ctx:
            if instance := await cls.perform_create(ctx, create_data):
                await cls._register_instances(ctx, [instance])
                return await cls._build_rela(ctx, instance, **kwargs)
        return None

    @classmethod
    async def get_or_create(cls, id_value: Any,
                            data: Union[CreateSchemaType, Dict[str, Any]], **kwargs) \
            -> Tuple[Optional['SqlModelBase'], bool]:
        if instance := await cls.get(id_value, **kwargs):
            return instance, False
        else:
            return await cls.create(data, **kwargs), True

    @classmethod
    async def update_by_id(cls, id_value: Any, data: Union[UpdateSchemaType, Dict[str, Any]], **kwargs) \
            -> Optional['SqlModelBase']:
        if isinstance(data, dict):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        if update_data:
            update_data = cls.prepare_for_update(update_data)

        async with cls._async_connection_context(begin_tx=True, autocommit=True) as ctx:
            if data := await cls.perform_update(ctx, update_data, id_value):
                if instance := await cls._construct(ctx, data, **kwargs):
                    await cls._register_instances(ctx, [instance])
                    return await cls._build_rela(ctx, instance, **kwargs)
        return None

    async def update(self, data: Union[UpdateSchemaType, Dict[str, Any]], **kwargs) -> bool:
        if isinstance(data, dict):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        if update_data:
            update_data = self.prepare_for_update(update_data)

        async with self._async_connection_context(begin_tx=True, autocommit=True) as ctx:
            if data := await self.perform_update(ctx, update_data, self.get_id_value()):
                load_fields = set(update_data.keys())
                await type(self)._construct(ctx, data, self, load_fields, **kwargs)
                await type(self)._build_rela(ctx, self, load_fields, **kwargs)
                return True

        return False

    @classmethod
    async def update_by(cls, filters: List[Any],
                        data: Union[UpdateSchemaType, Dict[str, Any]],
                        /, params: Dict[str, Any] = None, **kwargs) -> int:
        if isinstance(data, dict):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        if update_data:
            update_data = cls.prepare_for_update(update_data)

        query = cls.query_update(filters, params, **kwargs)
        async with cls._async_connection_context(begin_tx=True, autocommit=True) as ctx:
            return await cls.perform_update_by(ctx, update_data, query)

    @classmethod
    async def delete_by_id(cls, id_value: Any) -> bool:
        async with cls._async_connection_context(begin_tx=True, autocommit=True) as ctx:
            await cls._unregister_indices(ctx, [id_value])
            return await cls.perform_delete(ctx, id_value)

    async def delete(self) -> bool:
        async with self._async_connection_context(begin_tx=True, autocommit=True) as ctx:
            id_value = self.get_id_value()
            await self._unregister_indices(ctx, [id_value])
            return await self.perform_delete(ctx, id_value)

    @classmethod
    async def delete_by(cls, filters: List[Any], /, params: Dict[str, Any] = None, **kwargs) -> int:
        query = cls.query_delete(filters, params, **kwargs)
        async with cls._async_connection_context(begin_tx=True, autocommit=True) as ctx:
            return await cls.perform_delete_by(ctx, query)

    @classmethod
    def prepare_for_create(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        return data

    @classmethod
    def prepare_for_update(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        return data

    @classmethod
    def prepare_for_delete(cls, obj: 'SqlModelBase') -> 'SqlModelBase':
        return obj

    async def save(self, updated_fields: List[str] = None, **kwargs) -> bool:
        cols = self.get_columns()

        if updated_fields is not None and isinstance(updated_fields, Sequence):
            updated_fields = set(updated_fields)
            cols = [(col.name, col) for col in cols if self._get_field_by_column(col) in updated_fields]
            cols = ColumnCollection(columns=cols)

        col_values = self._get_column_values(cols, force_tuple=True)
        data = {k.name: v for k, v in zip(cols, col_values)}

        async with self._async_connection_context(begin_tx=True, autocommit=True) as ctx:
            if data := await self.perform_save(ctx, data, updated_fields or set(), **kwargs):
                self._assign(data)
            await self._register_instances(ctx, [self])
            await type(self)._build_rela(ctx, self, updated_fields, **kwargs)

        return len(data.keys()) > 0 if data else data is None

    async def load(self, field_names: List[str] = None) -> bool:
        query = self.query_get(self.get_id_value())
        field_names = set(field_names) if field_names else None
        async with self._async_connection_context() as ctx:
            if res := await self.perform_load(ctx, query, field_names):
                await type(self)._build_rela(ctx, self, field_names)
            return bool(res)

    @classmethod
    async def save_all(cls, objects: List['SqlModelBase'], **kwargs) -> bool:
        async with cls._async_connection_context(begin_tx=True, autocommit=True) as ctx:
            if res := await cls.perform_save_all(ctx, objects, **kwargs):
                await cls._register_instances(ctx, objects)
            return res

    #
    # Query operations
    #

    @classmethod
    def query_get(cls, id_value: Any, **kwargs):
        return cls._get_helper(id_value, **kwargs)

    @classmethod
    def query_list(cls, filters: List[Any], sorting: List[Any],
                   skip: int = 0, limit: int = 0, params: Dict[str, Any] = None, **kwargs):
        query = cls.query_for_select(**kwargs).offset(skip if skip >= 0 else 0)
        if limit > 0:
            query = query.limit(limit)
        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)
        for s in sorting:
            query = query.order_by(s)
        return query

    @classmethod
    def query_any(cls, indices: List[Any], **kwargs):
        return cls._get_any_helper(indices, **kwargs)

    # noinspection PyUnresolvedReferences
    @classmethod
    def query_count(cls, filters: Optional[List[Any]] = None, params: Dict[str, Any] = None, **kwargs):
        if filters:
            query = cls.query_for_select()
            for f in filters:
                query = query.where(f)
            if params:
                query = query.params(**params)
        else:
            query = cls.__table__

        return select([func.count(literal_column('1'))]).select_from(query.alias())

    @classmethod
    def query_exists(cls, id_value: Any, **kwargs):
        return cls._get_helper(id_value, query=exists(), **kwargs).select()

    @classmethod
    def query_exists_by(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs):
        query = exists(cls)

        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)

        return query.select()

    @classmethod
    def query_update(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs):
        query = cls.query_for_update(**kwargs)

        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)

        return query

    @classmethod
    def query_delete(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs):
        query = cls.query_for_delete(**kwargs)

        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)

        return query

    #
    # Perform operations
    #

    @classmethod
    async def perform_get(cls, ctx: ContextData, query, **kwargs) -> Optional['SqlModelBase']:
        raise NotImplementedError

    @classmethod
    async def perform_list(cls, ctx: ContextData, query, **kwargs) -> List['SqlModelBase']:
        raise NotImplementedError

    @classmethod
    async def perform_any(cls, ctx: ContextData, query, **kwargs) -> List[Optional['SqlModelBase']]:
        raise NotImplementedError

    @classmethod
    async def perform_count(cls, ctx: ContextData, query, **kwargs) -> int:
        raise NotImplementedError

    @classmethod
    async def perform_exists(cls, ctx: ContextData, query, **kwargs) -> bool:
        raise NotImplementedError

    @classmethod
    async def perform_exists_by(cls, ctx: ContextData, query, **kwargs) -> bool:
        raise NotImplementedError

    @classmethod
    async def perform_create(cls, ctx: ContextData, data: Dict[str, Any]) -> Optional['SqlModelBase']:
        raise NotImplementedError

    @classmethod
    async def perform_update(
            cls, ctx: ContextData, data: Dict[str, Any], id_value: Any) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    @classmethod
    async def perform_update_by(cls, ctx: ContextData, data: Dict[str, Any], query) -> int:
        raise NotImplementedError

    @classmethod
    async def perform_delete(cls, ctx: ContextData, id_value: Any) -> bool:
        raise NotImplementedError

    @classmethod
    async def perform_delete_by(cls, ctx: ContextData, query) -> int:
        raise NotImplementedError

    async def perform_save(
        self, ctx: ContextData, data: Dict[str, Any], updated_fields: Set[str], **kwargs) \
            -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    async def perform_load(self, ctx: ContextData, query, field_names: List[str] = None) -> bool:
        raise NotImplementedError

    @classmethod
    async def perform_save_all(cls, ctx: ContextData, objects: List['SqlModelBase'], **kwargs) -> bool:
        raise NotImplementedError

    #
    # Private
    #

    # noinspection PyUnresolvedReferences
    @classmethod
    def _get_id_columns(cls) -> ColumnCollection:
        return cls.__table__.primary_key.columns

    # noinspection PyTypeChecker
    def _get_column_values(
            self, columns: ColumnCollection, force_tuple: bool = False) -> Union[Any, Tuple[Any]]:
        rv = []
        for c in columns:
            rv.append(getattr(self, self._get_field_by_column(c)))
        return rv[0] if len(rv) == 1 and not force_tuple else tuple(rv)

    @classmethod
    def _get_field_by_column(cls, c: Column) -> str:
        raise NotImplementedError

    # noinspection PyUnresolvedReferences
    @classmethod
    def _get_fk_columns(cls, model) -> ColumnCollection:
        for fk in cls.__table__.foreign_keys:
            if model.__table__ == fk.constraint.referred_table:
                return fk.constraint.columns
        return ColumnCollection()

    @classmethod
    def _get_helper(cls, ident: Any, query=None, **kwargs):
        cls._check_abstract()
        if not isinstance(ident, (list, tuple, dict)):
            ident_ = [ident]
        else:
            ident_ = ident
        columns = cls._get_id_columns()
        if len(ident_) != len(columns):
            raise ValueError(
                f'Incorrect number of values as primary key: expected {len(columns)}, got {len(ident_)}.')

        clause = query if query is not None else cls.query_for_select(**kwargs)
        for i, c in enumerate(columns):
            try:
                val = ident_[i]
            except KeyError:
                val = ident_[cls._get_field_by_column(c)]
            clause = clause.where(c == val)
        return clause

    @classmethod
    def _get_any_helper(cls, indices: List[Any], query=None, **kwargs):
        cls._check_abstract()
        columns = cls._get_id_columns()
        clause = query if query is not None else cls.query_for_select(**kwargs)
        vals_clause = []

        for ident in indices:
            if not isinstance(ident, (list, tuple, dict)):
                ident_ = [ident]
            else:
                ident_ = ident

            if len(ident_) != len(columns):
                raise ValueError(
                    f'Incorrect number of values as primary key: expected {len(columns)}, got {len(ident_)}.')

            vals = []
            for i, c in enumerate(columns):
                try:
                    val = ident_[i]
                except KeyError:
                    val = ident_[cls._get_field_by_column(c)]
                vals.append(val)

            if len(vals) == 1:
                vals_clause.append(vals[0])
            elif len(vals) > 1:
                vals_clause.append((*vals,))

        if len(columns) == 1:
            clause = clause.where(columns[columns.keys()[0]].in_(vals_clause))
        elif len(columns) > 1:
            clause = clause.where(tuple_(*columns).in_(vals_clause))
        return clause

    @classmethod
    async def _get_from_orm_cache(cls, ctx: ContextData, indices: List[Any]) -> List[Optional['SqlModelBase']]:
        return [None for _ in indices]

    @classmethod
    async def _attach_to_session(cls, ctx: ContextData, objects: List['SqlModelBase']):
        pass
