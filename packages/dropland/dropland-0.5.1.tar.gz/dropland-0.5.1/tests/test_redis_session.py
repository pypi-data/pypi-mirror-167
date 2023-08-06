import pytest

from dropland.blocks.redis import USE_REDIS

pytestmark = pytest.mark.skipif(not USE_REDIS, reason='For Redis only')

if USE_REDIS:
    from dropland.blocks.redis.containers import RedisStorage, SingleRedisStorage, MultipleRedisStorage
    from dropland.blocks.redis.engine import EngineConfig
    from tests import REDIS_URI


def test_session_connections(test_redis_storage, redis_engine, redis_session):
    assert not redis_session.get_connection('_')

    conn_data = redis_session.get_connection('dropland')
    assert conn_data
    assert conn_data.engine is redis_engine
    assert conn_data.connection

    created, conn_data = redis_session.get_or_create_connection('dropland')
    assert not created
    assert conn_data
    assert conn_data.engine is redis_engine
    assert conn_data.connection

    assert not test_redis_storage.get_connection('_')
    assert test_redis_storage.get_connection('dropland') is conn_data


@pytest.mark.asyncio
async def test_container_connections():
    config = EngineConfig(url=REDIS_URI)

    cont = RedisStorage()
    engine = cont.create_engine('dropland', config)
    await cont.session.init()

    conn_data = cont.get_connection('dropland')
    assert conn_data
    assert conn_data.engine is engine
    assert conn_data.connection
    assert not cont.get_connection('_')
    cont.unwire()

    cont = SingleRedisStorage()
    cont.config.from_dict({
        'name': 'dropland1',
        'engine_config': config
    })
    engine = cont.create_engine()
    await cont.session.init()

    conn_data = cont.get_connection()
    assert conn_data
    assert conn_data.engine is engine
    assert conn_data.connection
    cont.unwire()

    cont = MultipleRedisStorage()
    cont.config.from_dict({
        'one': {
            'name': 'dropland1',
            'engine_config': config
        },
        'two': {
            'name': 'dropland2',
            'engine_config': config
        },
    })
    engine1 = cont.create_engine('one')
    engine2 = cont.create_engine('two')
    await cont.session.init()

    for name, engine in zip(('one', 'two'), (engine1, engine2)):
        conn_data = cont.get_connection(name)
        assert conn_data
        assert conn_data.engine is engine
        assert conn_data.connection

    assert not cont.get_connection('_')
    cont.unwire()
