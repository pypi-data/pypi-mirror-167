from functools import partial

from dropland.util import invoke_async, invoke_sync

from .redis import USE_REDIS
from .rmq import USE_RMQ
from .sql import USE_SQL


def sync_resource_session(func, *args, **kwargs):
    if USE_SQL:
        from .sql.containers import sync_resource_session

        func = partial(sync_resource_session, func, *args, **kwargs)

    return invoke_sync(func)


async def async_resource_session(func, *args, **kwargs):
    if USE_RMQ:
        from .rmq.containers import async_resource_session

        func = partial(async_resource_session, func, *args, **kwargs)

    if USE_REDIS:
        from .redis.containers import async_resource_session

        func = partial(async_resource_session, func, *args, **kwargs)

    if USE_SQL:
        from .sql.containers import async_resource_session

        func = partial(async_resource_session, func, *args, **kwargs)

    return await invoke_async(func)
