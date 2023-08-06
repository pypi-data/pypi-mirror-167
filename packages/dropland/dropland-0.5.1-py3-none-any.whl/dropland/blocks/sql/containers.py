from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from dropland.util import default_value, invoke_async, invoke_sync
from .engine import EngineConfig, EngineFactory
from .loader import SqlBackendLoader
from .session import SessionManager


class SqlStorage(containers.DeclarativeContainer):
    __self__ = providers.Self()
    backend_loader = providers.Singleton(SqlBackendLoader)
    engine_factory = providers.Singleton(EngineFactory, backend_loader)
    manager = providers.Singleton(SessionManager, engine_factory)

    def _create_engine(self, *args, **kwargs):
        return self.engine_factory().create_engine(*args, **kwargs)

    def _init_session(self, begin_tx: bool = True, autocommit: bool = True):
        with self.manager().init_engines(begin_tx=begin_tx, autocommit=autocommit):
            yield self.manager()

    async def _init_async_session(self, begin_tx: bool = True, autocommit: bool = True):
        async with self.manager().init_async_engines(begin_tx=begin_tx, autocommit=autocommit):
            yield self.manager()

    create_engine = providers.Factory(_create_engine, __self__)
    session = providers.Resource(_init_session, __self__)
    async_session = providers.Resource(_init_async_session, __self__)
    get_connection = providers.Factory(manager.provided.get_connection.call())

    wiring_config = containers.WiringConfiguration(
        modules=['.model', __name__]
    )


class SingleSqlStorage(SqlStorage):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self):
        if isinstance(self.config.engine_config(), EngineConfig):
            engine_config = self.config.engine_config()
        else:
            engine_config = EngineConfig(
                url=self.config.engine_config.url(),
                echo=self.config.engine_config.echo.as_(bool)(),
                pool_min_size=self.config.engine_config.
                    pool_min_size.as_(default_value(int))(default=1),
                pool_max_size=self.config.engine_config.
                    pool_max_size.as_(default_value(int))(default=8),
                pool_expire_seconds=self.config.engine_config.
                    pool_expire_seconds.as_(default_value(int))(default=60),
                pool_timeout_seconds=self.config.engine_config.
                    pool_timeout_seconds.as_(default_value(int))(default=15)
            )
        return SqlStorage._create_engine(
            self, self.config.db_type(), engine_config, backend_name=self.config.backend_name(),
            use_async=self.config.use_async.as_(bool)())

    create_engine = providers.Factory(_create_engine, __self__)
    session = providers.Resource(SqlStorage._init_session, __self__)
    async_session = providers.Resource(SqlStorage._init_async_session, __self__)
    get_connection = providers.Factory(
        SqlStorage.get_connection, config.db_type, config.backend_name, config.use_async)

    wiring_config = containers.WiringConfiguration(
        modules=['.model', __name__]
    )


class MultipleSqlStorage(SqlStorage):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self, name: str):
        if conf := self.config.get(name):
            if isinstance(conf['engine_config'], EngineConfig):
                engine_config = conf['engine_config']
            else:
                engine_config = EngineConfig(
                    url=conf['engine_config']['url'],
                    echo=bool(conf['engine_config'].get('echo')),
                    pool_min_size=int(conf['engine_config'].get('pool_min_size', 1)),
                    pool_max_size=int(conf['engine_config'].get('pool_max_size', 8)),
                    pool_expire_seconds=int(conf['engine_config'].get('pool_expire_seconds', 60)),
                    pool_timeout_seconds=int(conf['engine_config'].get('pool_timeout_seconds', 15))
                )
            return SqlStorage._create_engine(
                self, conf['db_type'], engine_config, backend_name=conf.get('backend_name'),
                use_async=conf.get('use_async', False))
        return None

    def _get_connection(self, name: str):
        if conf := self.config.get(name):
            return self.manager().get_connection(
                conf['db_type'], backend_name=conf.get('backend_name'),
                is_async=conf.get('use_async', False))
        return None

    create_engine = providers.Factory(_create_engine, __self__)
    session = providers.Resource(SqlStorage._init_session, __self__)
    async_session = providers.Resource(SqlStorage._init_async_session, __self__)
    get_connection = providers.Factory(_get_connection, __self__)

    wiring_config = containers.WiringConfiguration(
        modules=['.model', __name__]
    )


default_sql_storage = SqlStorage()


@inject
def sync_resource_session(func, begin_tx: bool = True, autocommit: bool = True,
                          resource: SqlStorage = Provide['<container>'], *args, **kwargs):
    if not isinstance(resource, (SqlStorage, containers.DynamicContainer)):
        return invoke_sync(func)

    resource.session(begin_tx=begin_tx, autocommit=autocommit)
    try:
        return invoke_sync(func)
    finally:
        resource.session.shutdown()


@inject
async def async_resource_session(func, begin_tx: bool = True, autocommit: bool = True,
                                 resource: SqlStorage = Provide['<container>'], *args, **kwargs):
    if not isinstance(resource, (SqlStorage, containers.DynamicContainer)):
        return await invoke_async(func)

    await resource.async_session(begin_tx=begin_tx, autocommit=autocommit)
    try:
        return await invoke_async(func)
    finally:
        await resource.async_session.shutdown()
