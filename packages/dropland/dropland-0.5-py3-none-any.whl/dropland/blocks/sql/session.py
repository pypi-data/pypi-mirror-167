import contextlib
from collections import defaultdict
from dataclasses import dataclass, replace
from typing import Any, Dict, List, Mapping, Optional, Sequence, Set, Tuple

from contextvars import ContextVar

from .base import SqlStorageEngine, SqlStorageType
from .engine import EngineFactory, EngineKey


@dataclass
class ConnectionData:
    engine: SqlStorageEngine
    connection: Any
    timeout_secs: int
    in_transaction: bool = False


class ConnectionContext:
    def __init__(self):
        self.conns: Dict[EngineKey, ConnectionData] = dict()
        self.conns_by_type: Dict[SqlStorageType, Set[str]] = defaultdict(set)
        self.conns_by_backend: Dict[str, Set[SqlStorageType]] = defaultdict(set)


class SessionManager:
    def __init__(self, engine_factory: EngineFactory):
        self._ctx: ContextVar[ConnectionContext] = ContextVar('_ctx', default=ConnectionContext())
        self._engine_factory = engine_factory

    @contextlib.contextmanager
    def set_context(self, ctx: ConnectionContext):
        token = self._ctx.set(ctx)
        yield
        self._ctx.reset(token)

    def get_connection(self, db_type: SqlStorageType, backend_name: str, is_async: bool) -> Optional[ConnectionData]:
        return self._ctx.get().conns.get(EngineKey(db_type=db_type, backend=backend_name, is_async=is_async))

    def get_connections_for_type(self, db_type: SqlStorageType, is_async: bool) -> List[ConnectionData]:
        backends = self._ctx.get().conns_by_type.get(db_type, set())
        conns = [self.get_connection(db_type, b, is_async) for b in backends]
        return [c for c in conns if c is not None]

    def get_connections_for_backend(self, backend_name: str, is_async: bool) -> List[ConnectionData]:
        db_types = self._ctx.get().conns_by_backend.get(backend_name, set())
        conns = [self.get_connection(t, backend_name, is_async) for t in db_types]
        return [c for c in conns if c is not None]

    def get_or_create_connection(
        self, db_type: SqlStorageType, backend_name: str, is_async: bool,
            timeout_secs: Optional[int] = None) -> Tuple[bool, Optional[ConnectionData]]:
        if conn := self.get_connection(db_type, backend_name, is_async):
            return False, conn

        if engine := self._engine_factory.get_engine(db_type, backend_name, is_async):
            return True, ConnectionData(
                engine=engine, connection=engine.new_connection(),
                timeout_secs=timeout_secs or engine.timeout.total_seconds())

        return False, None

    @contextlib.contextmanager
    def connection_context(
        self, db_type: SqlStorageType, backend_name: str,
            begin_tx: bool = True, autocommit: bool = True, timeout_secs: Optional[int] = None):
        created, data = self.get_or_create_connection(db_type, backend_name, False, timeout_secs)

        if not created:
            if begin_tx and not data.in_transaction:
                with data.engine.transaction_context(data.connection, autocommit):
                    yield self._add_connection(db_type, backend_name, False, replace(data, in_transaction=True))
                    self._add_connection(db_type, backend_name, False, replace(data, in_transaction=False))
            else:
                yield data
            return

        with data.connection as conn:
            assert isinstance(conn, data.engine.backend.connection_class), \
                f'Engine for DB "{db_type.value}" and backend "{backend_name}" has only async driver, ' \
                f'use async_connection_context() function instead'

            data = replace(data, connection=conn, in_transaction=begin_tx)
            if begin_tx:
                with data.engine.transaction_context(data.connection, autocommit):
                    yield self._add_connection(db_type, backend_name, False, data)
            else:
                yield self._add_connection(db_type, backend_name, False, data)
            self._remove_connection(db_type, backend_name, False)

    @contextlib.asynccontextmanager
    async def async_connection_context(
        self, db_type: SqlStorageType, backend_name: str,
            begin_tx: bool = True, autocommit: bool = True, timeout_secs: Optional[int] = None):
        created, data = self.get_or_create_connection(db_type, backend_name, True, timeout_secs)

        if not created:
            if begin_tx and not data.in_transaction:
                async with data.engine.async_transaction_context(data.connection, autocommit):
                    yield self._add_connection(db_type, backend_name, True, replace(data, in_transaction=True))
                    self._add_connection(db_type, backend_name, True, replace(data, in_transaction=False))
            else:
                yield data
            return

        async with data.connection as conn:
            assert isinstance(conn, data.engine.backend.async_connection_class), \
                f'Engine for DB "{db_type.value}" and backend "{backend_name}" has only sync driver, ' \
                f'use connection_context() function instead'

            data = replace(data, connection=conn, in_transaction=begin_tx)
            if begin_tx:
                async with data.engine.async_transaction_context(data.connection, autocommit):
                    yield self._add_connection(db_type, backend_name, True, data)
            else:
                yield self._add_connection(db_type, backend_name, True, data)
            self._remove_connection(db_type, backend_name, True)

    @contextlib.contextmanager
    def init_engines(self, engines: Mapping[str, Sequence[SqlStorageEngine]] = None,
                     begin_tx: bool = True, autocommit: bool = True):
        engines = self._engine_factory.get_engines(engines or [], False)
        with contextlib.ExitStack() as stack:
            for backend_name, engine_list in engines.items():
                for engine in engine_list:
                    engine.start()
                    stack.callback(engine.stop)
                    stack.enter_context(self.connection_context(engine.db_type, backend_name, begin_tx, autocommit))
            yield self._ctx.get()

    @contextlib.asynccontextmanager
    async def init_async_engines(self, engines: Mapping[str, Sequence[SqlStorageEngine]] = None,
                                 begin_tx: bool = True, autocommit: bool = True):
        engines = self._engine_factory.get_engines(engines or [], True)
        async with contextlib.AsyncExitStack() as stack:
            for backend_name, engine_list in engines.items():
                for engine in engine_list:
                    if engine.is_async:
                        await engine.async_start()
                        stack.push_async_callback(engine.async_stop)
                    else:
                        engine.start()
                        stack.callback(engine.stop)

                    await stack.enter_async_context(
                        self.async_connection_context(engine.db_type, backend_name, begin_tx, autocommit)
                    )
            yield self._ctx.get()

    def _add_connection(
            self, db_type: SqlStorageType, backend_name: str, is_async: bool, data: ConnectionData) -> ConnectionData:
        ctx = self._ctx.get()
        ctx.conns[EngineKey(db_type=db_type, backend=backend_name, is_async=is_async)] = data
        ctx.conns_by_type[db_type].add(backend_name)
        ctx.conns_by_backend[backend_name].add(db_type)
        return data

    def _remove_connection(self, db_type: SqlStorageType, backend_name: str, is_async: bool):
        ctx = self._ctx.get()
        ctx.conns.pop(EngineKey(db_type=db_type, backend=backend_name, is_async=is_async))
        ctx.conns_by_type[db_type].remove(backend_name)
        ctx.conns_by_backend[backend_name].remove(db_type)
