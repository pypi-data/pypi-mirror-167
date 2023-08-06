import aio_pika
import pytest
from dropland.blocks.rmq import USE_RMQ

pytestmark = pytest.mark.skipif(not USE_RMQ, reason='For RabbitMQ only')

if USE_RMQ:
    from dropland.blocks.rmq.containers import RmqStorage, SingleRmqStorage, MultipleRmqStorage, \
        default_rmq_storage
    from dropland.blocks.rmq.engine import EngineConfig, RmqStorageEngine
    from tests import RMQ_URI


@pytest.mark.asyncio
async def test_create_engine():
    engine_factory = default_rmq_storage.engine_factory()

    assert not engine_factory.get_engine('')

    config = EngineConfig(url=RMQ_URI)
    assert engine_factory.create_engine('dropland', config)

    engine = engine_factory.get_engine('dropland')
    assert engine
    assert engine.backend is engine_factory
    assert engine.is_async

    assert engine_factory.get_engine_names() == ['dropland']


@pytest.mark.asyncio
async def test_create_connection():
    engine_factory = default_rmq_storage.engine_factory()

    config = EngineConfig(url=RMQ_URI)
    engine = engine_factory.create_engine('dropland', config)

    assert engine
    await engine.async_start()

    async with engine.new_connection() as channel:
        queue = await channel.declare_queue('test', auto_delete=True)
        await channel.default_exchange.publish(
            aio_pika.Message(body=b'12345'),
            routing_key='test',
        )
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    assert message.body == b'12345'
                break

    await engine.async_stop()


@pytest.mark.asyncio
async def test_session_connections():
    config = EngineConfig(url=RMQ_URI)

    rmq_storage = SingleRmqStorage()
    rmq_storage.config.from_dict({
        'name': 'dropland1',
        'engine_config': config
    })

    assert rmq_storage.create_engine()
    session = await rmq_storage.session()
    conn_data = rmq_storage.get_connection()
    conn_data1 = session.get_connection('dropland1')
    assert rmq_storage.manager().get_connection('dropland1') == conn_data == conn_data1


@pytest.mark.asyncio
async def test_storage_container():
    config = EngineConfig(url=RMQ_URI)

    cont = RmqStorage()

    eng = cont.create_engine('dropland', config)
    assert isinstance(eng, RmqStorageEngine)
    assert eng.name == 'dropland'
    cont.unwire()

    cont = SingleRmqStorage()
    cont.config.from_dict({
        'name': 'dropland1',
        'engine_config': config
    })
    eng1 = cont.create_engine()
    eng2 = cont.create_engine()
    assert eng1 is eng2
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

    eng1 = cont.create_engine('one')
    eng2 = cont.create_engine('two')
    assert eng1 is not eng2
    assert eng1.is_async is True
    assert eng2.is_async is True
    assert eng1.name == 'dropland1'
    assert eng2.name == 'dropland2'

    cont.unwire()
