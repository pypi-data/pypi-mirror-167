from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from dropland.util import default_value, invoke_async

from .engine import EngineConfig, RmqStorageBackend
from .session import SessionManager


class RmqStorage(containers.DeclarativeContainer):
    __self__ = providers.Self()
    engine_factory = providers.Singleton(RmqStorageBackend)
    manager = providers.Singleton(SessionManager, engine_factory)

    def _create_engine(self, *args, **kwargs):
        return self.engine_factory().create_engine(*args, **kwargs)

    async def _init_async_session(self):
        async with self.manager().init_async_engines():
            yield self.manager()

    create_engine = providers.Factory(_create_engine, __self__)
    session = providers.Resource(_init_async_session, __self__)
    get_connection = providers.Factory(manager.provided.get_connection.call())

    wiring_config = containers.WiringConfiguration(
        modules=[__name__]
    )


class SingleRmqStorage(RmqStorage):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self):
        if isinstance(self.config.engine_config(), EngineConfig):
            engine_config = self.config.engine_config()
        else:
            engine_config = EngineConfig(
                url=self.config.engine_config.url(),
                virtualhost=self.config.engine_config.virtualhost(),
                timeout_seconds=self.config.engine_config.
                    timeout_seconds.as_(default_value(int))(default=5),
                pool_max_connections=self.config.engine_config.
                    pool_max_connections.as_(default_value(int))(default=4),
                pool_max_channels_per_connection=self.config.engine_config.
                    pool_max_channels_per_connection.as_(default_value(int))(default=100)
            )
        return RmqStorage._create_engine(self, self.config.name(), engine_config)

    create_engine = providers.Factory(_create_engine, __self__)
    session = providers.Resource(RmqStorage._init_async_session, __self__)
    get_connection = providers.Factory(RmqStorage.get_connection, config.name)

    wiring_config = containers.WiringConfiguration(
        modules=[__name__]
    )


class MultipleRmqStorage(RmqStorage):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self, name: str):
        if conf := self.config.get(name):
            if isinstance(conf['engine_config'], EngineConfig):
                engine_config = conf['engine_config']
            else:
                engine_config = EngineConfig(
                    url=conf['engine_config']['url'],
                    virtualhost=conf['engine_config']['virtualhost'],
                    timeout_seconds=int(conf['engine_config'].get('timeout_seconds', 5)),
                    pool_max_connections=int(conf['engine_config'].get('pool_max_connections', 4)),
                    pool_max_channels_per_connection=int(conf['engine_config'].get(
                        'pool_max_channels_per_connection', 100))
                )
            return RmqStorage._create_engine(self, conf['name'], engine_config)
        return None

    def _get_connection(self, name: str):
        if conf := self.config.get(name):
            return self.manager().get_connection(conf['name'])
        return None

    create_engine = providers.Factory(_create_engine, __self__)
    session = providers.Resource(RmqStorage._init_async_session, __self__)
    get_connection = providers.Factory(_get_connection, __self__)

    wiring_config = containers.WiringConfiguration(
        modules=[__name__]
    )


default_rmq_storage = RmqStorage()


@inject
async def async_resource_session(func, resource: RmqStorage = Provide['<container>'], *args, **kwargs):
    if not isinstance(resource, (RmqStorage, containers.DynamicContainer)):
        return await invoke_async(func)

    await resource.session()
    try:
        return await invoke_async(func)
    finally:
        await resource.session.shutdown()
