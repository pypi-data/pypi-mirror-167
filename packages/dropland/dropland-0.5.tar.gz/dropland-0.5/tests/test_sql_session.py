import pytest

from tests.sql_models_data import USE_SQLA

pytestmark = pytest.mark.skipif(not USE_SQLA, reason='For SqlAlchemy only')

if USE_SQLA:
    from dropland.blocks.sql.containers import MultipleSqlStorage, SingleSqlStorage, SqlStorage
    from dropland.blocks.sql.engine import SqlStorageType, EngineConfig
    from tests import SQLITE_URI


def test_sync_session_connections(test_sql_storage, sql_sync_engine, sync_sql_session):
    assert sync_sql_session.get_connection(SqlStorageType.SQLITE, 'sqla', False)
    assert not sync_sql_session.get_connection(SqlStorageType.SQLITE, 'sqla', True)

    for c in sync_sql_session.get_connections_for_type(SqlStorageType.SQLITE, False):
        assert c.engine is sql_sync_engine
        assert c.connection
        assert c.in_transaction

    assert 0 == len(sync_sql_session.get_connections_for_type(SqlStorageType.SQLITE, True))

    for c in sync_sql_session.get_connections_for_backend('sqla', False):
        assert c.engine is sql_sync_engine
        assert c.connection
        assert c.in_transaction

    assert 0 == len(sync_sql_session.get_connections_for_backend('sqla', True))

    created, sql_data = sync_sql_session.get_or_create_connection(SqlStorageType.SQLITE, 'sqla', False)
    assert not created
    assert sql_data
    assert sql_data.engine is sql_sync_engine
    assert sql_data.connection
    assert sql_data.in_transaction

    assert not test_sql_storage.get_connection(SqlStorageType.SQLITE, 'sqla', True)
    assert test_sql_storage.get_connection(SqlStorageType.SQLITE, 'sqla', False) is sql_data


@pytest.mark.asyncio
async def test_async_session_connections(test_sql_storage, sql_async_engine, async_sql_session):
    assert not async_sql_session.get_connection(SqlStorageType.SQLITE, 'sqla', False)
    assert async_sql_session.get_connection(SqlStorageType.SQLITE, 'sqla', True)

    assert 0 == len(async_sql_session.get_connections_for_type(SqlStorageType.SQLITE, False))

    for c in async_sql_session.get_connections_for_type(SqlStorageType.SQLITE, True):
        assert c.engine is sql_async_engine
        assert c.connection
        assert c.in_transaction

    assert 0 == len(async_sql_session.get_connections_for_backend('sqla', False))

    for c in async_sql_session.get_connections_for_backend('sqla', True):
        assert c.engine is sql_async_engine
        assert c.connection
        assert c.in_transaction

    created, sql_data = async_sql_session.get_or_create_connection(SqlStorageType.SQLITE, 'sqla', True)
    assert not created
    assert sql_data
    assert sql_data.engine is sql_async_engine
    assert sql_data.connection
    assert sql_data.in_transaction

    assert not test_sql_storage.get_connection(SqlStorageType.SQLITE, 'sqla', False)
    assert test_sql_storage.get_connection(SqlStorageType.SQLITE, 'sqla', True) is sql_data


def test_sync_container_connections():
    sqlite_config = EngineConfig(
        url=SQLITE_URI,
        pool_min_size=1, pool_max_size=2,
        pool_expire_seconds=15, pool_timeout_seconds=15,
    )

    cont = SqlStorage()
    engine = cont.create_engine(SqlStorageType.SQLITE, sqlite_config, use_async=False)
    cont.session.init()

    conn_data = cont.get_connection(SqlStorageType.SQLITE, 'sqla', is_async=False)
    assert conn_data
    assert conn_data.engine is engine
    assert conn_data.connection
    assert not cont.get_connection(SqlStorageType.SQLITE, 'sqla', is_async=True)
    cont.unwire()

    cont = SingleSqlStorage()
    cont.config.from_dict({
        'db_type': SqlStorageType.SQLITE,
        'engine_config': sqlite_config,
        'use_async': False,
        'backend_name': 'sqla'
    })
    engine = cont.create_engine()
    cont.session.init()

    conn_data = cont.get_connection()
    assert conn_data
    assert conn_data.engine is engine
    assert conn_data.connection
    cont.unwire()

    cont = MultipleSqlStorage()
    cont.config.from_dict({
        'one': {
            'db_type': SqlStorageType.SQLITE,
            'engine_config': sqlite_config,
            'use_async': False,
            'backend_name': 'sqla'
        },
        'two': {
            'db_type': SqlStorageType.SQLITE,
            'engine_config': sqlite_config,
            'use_async': False,
            'backend_name': 'sqla'
        },
    })
    engine1 = cont.create_engine('one')
    engine2 = cont.create_engine('two')
    cont.session.init()

    for name, engine in zip(('one', 'two'), (engine1, engine2)):
        conn_data = cont.get_connection(name)
        assert conn_data
        assert conn_data.engine is engine
        assert conn_data.connection

    assert not cont.get_connection('_')
    cont.unwire()


@pytest.mark.asyncio
async def test_async_container_connections():
    sqlite_config = EngineConfig(
        url=SQLITE_URI,
        pool_min_size=1, pool_max_size=2,
        pool_expire_seconds=15, pool_timeout_seconds=15,
    )

    cont = SqlStorage()
    engine = cont.create_engine(SqlStorageType.SQLITE, sqlite_config, use_async=True)
    await cont.async_session.init()

    conn_data = cont.get_connection(SqlStorageType.SQLITE, 'sqla', is_async=True)
    assert conn_data
    assert conn_data.engine is engine
    assert conn_data.connection
    assert not cont.get_connection(SqlStorageType.SQLITE, 'sqla', is_async=False)
    cont.unwire()

    cont = SingleSqlStorage()
    cont.config.from_dict({
        'db_type': SqlStorageType.SQLITE,
        'engine_config': sqlite_config,
        'use_async': True,
        'backend_name': 'sqla'
    })
    engine = cont.create_engine()
    await cont.async_session.init()

    conn_data = cont.get_connection()
    assert conn_data
    assert conn_data.engine is engine
    assert conn_data.connection
    cont.unwire()

    cont = MultipleSqlStorage()
    cont.config.from_dict({
        'one': {
            'db_type': SqlStorageType.SQLITE,
            'engine_config': sqlite_config,
            'use_async': True,
            'backend_name': 'sqla'
        },
        'two': {
            'db_type': SqlStorageType.SQLITE,
            'engine_config': sqlite_config,
            'use_async': True,
            'backend_name': 'sqla'
        },
    })
    engine1 = cont.create_engine('one')
    engine2 = cont.create_engine('two')
    await cont.async_session.init()

    for name, engine in zip(('one', 'two'), (engine1, engine2)):
        conn_data = cont.get_connection(name)
        assert conn_data
        assert conn_data.engine is engine
        assert conn_data.connection

    assert not cont.get_connection('_')
    cont.unwire()
