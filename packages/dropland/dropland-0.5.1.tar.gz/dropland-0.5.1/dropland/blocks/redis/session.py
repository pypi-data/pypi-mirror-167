import contextlib
from dataclasses import dataclass, replace
from typing import Dict, List, Optional, Tuple

from aioredis import Redis as RedisConnection
from contextvars import ContextVar

from .engine import RedisStorageBackend, RedisStorageEngine


@dataclass
class ConnectionData:
    engine: RedisStorageEngine
    connection: RedisConnection


class ConnectionContext:
    def __init__(self):
        self.conns: Dict[str, ConnectionData] = dict()


class SessionManager:
    def __init__(self, engine_factory: RedisStorageBackend):
        self._ctx: ContextVar[ConnectionContext] = ContextVar('_ctx', default=ConnectionContext())
        self._engine_factory = engine_factory

    @contextlib.contextmanager
    def set_context(self, ctx: ConnectionContext):
        token = self._ctx.set(ctx)
        yield
        self._ctx.reset(token)

    def get_connection(self, name: str) -> Optional[ConnectionData]:
        return self._ctx.get().conns.get(name)

    def get_or_create_connection(self, name: str) -> Tuple[bool, Optional[ConnectionData]]:
        if conn := self.get_connection(name):
            return False, conn

        if engine := self._engine_factory.get_engine(name):
            return True, ConnectionData(
                engine=engine,
                connection=engine.new_connection())

        return False, None

    @contextlib.asynccontextmanager
    async def async_connection_context(self, name: str):
        created, data = self.get_or_create_connection(name)

        if not created:
            yield data
            return

        async with data.connection as conn:
            data = replace(data, connection=conn)
            yield self._add_connection(name, data)
            self._remove_connection(name)

    @contextlib.asynccontextmanager
    async def init_async_engines(self, names: List[str] = None):
        engines = self._engine_factory.get_engines(names or [])
        async with contextlib.AsyncExitStack() as stack:
            for name, engine in engines.items():
                assert engine is self._engine_factory.get_engine(name)
                if engine.is_async:
                    await engine.async_start()
                    stack.push_async_callback(engine.async_stop)
                else:
                    engine.start()
                    stack.callback(engine.stop)

                await stack.enter_async_context(self.async_connection_context(name))
            yield self._ctx.get()

    def _add_connection(self, name: str, data: ConnectionData) -> ConnectionData:
        self._ctx.get().conns[name] = data
        return data

    def _remove_connection(self, name: str):
        self._ctx.get().conns.pop(name)
