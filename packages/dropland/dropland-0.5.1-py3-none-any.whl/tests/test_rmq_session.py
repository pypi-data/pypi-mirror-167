import pytest

from dropland.blocks.rmq import USE_RMQ

pytestmark = pytest.mark.skipif(not USE_RMQ, reason='For RabbitMQ only')

if USE_RMQ:
    from dropland.blocks.rmq.containers import RmqStorage, SingleRmqStorage, MultipleRmqStorage
    from dropland.blocks.rmq.engine import EngineConfig
    from tests import RMQ_URI


def test_session_connections(test_rmq_storage, rmq_engine, rmq_session):
    assert not rmq_session.get_connection('_')

    conn_data = rmq_session.get_connection('dropland')
    assert conn_data
    assert conn_data.engine is rmq_engine
    assert conn_data.connection

    created, conn_data = rmq_session.get_or_create_connection('dropland')
    assert not created
    assert conn_data
    assert conn_data.engine is rmq_engine
    assert conn_data.connection

    assert not test_rmq_storage.get_connection('_')
    assert test_rmq_storage.get_connection('dropland') is conn_data


@pytest.mark.asyncio
async def test_container_connections():
    config = EngineConfig(url=RMQ_URI)

    cont = RmqStorage()
    engine = cont.create_engine('dropland', config)
    await cont.session.init()

    conn_data = cont.get_connection('dropland')
    assert conn_data
    assert conn_data.engine is engine
    assert conn_data.connection
    assert not cont.get_connection('_')
    cont.unwire()

    cont = SingleRmqStorage()
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

    cont = MultipleRmqStorage()
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
