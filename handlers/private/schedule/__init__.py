from aiogram import Router


def get_schedule_router() -> Router:
    from . import schedule

    router = Router()
    router.include_router(schedule.router)

    return router

