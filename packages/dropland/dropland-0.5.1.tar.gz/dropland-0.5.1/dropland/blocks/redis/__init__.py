try:
    import aioredis

    from .model import SimpleRedisModelBase as SimpleRedisModel, HashRedisModelBase as HashRedisModel
    from .engine import EngineConfig, RedisStorageBackend, RedisStorageEngine
    from .session import SessionManager
    from .settings import RedisSettings

    USE_REDIS = True

except ImportError:
    USE_REDIS = False
