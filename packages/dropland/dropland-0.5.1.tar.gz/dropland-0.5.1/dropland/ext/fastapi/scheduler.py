from dropland.blocks.scheduler import Scheduler, USE_SCHEDULER
from dropland.log import logger, tr
from fastapi import FastAPI


def add_scheduler(app: FastAPI, scheduler: Scheduler):
    if not USE_SCHEDULER:
        return

    @app.on_event('startup')
    def init_task():
        app.state.scheduler = scheduler
        if not scheduler.running:
            scheduler.start()

        logger.info(tr('dropland.blocks.scheduler.started'))

    @app.on_event('shutdown')
    def fini_task():
        scheduler.shutdown(wait=True)
        app.state.scheduler = None

        logger.info(tr('dropland.blocks.scheduler.stopped'))
