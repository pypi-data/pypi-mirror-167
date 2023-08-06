try:
    import aioredis

    from .engine import EngineConfig, SchedulerBackend
    from .local import Scheduler
    from .service import SchedulerService
    from .settings import SchedulerSettings

    USE_SCHEDULER = True

except ImportError:
    USE_SCHEDULER = False
