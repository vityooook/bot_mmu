from aiogram import Router


def get_handlers_router() -> Router:
    from .groups.start import router as group_start
    from .groups.schedule import router as group_schedule
    from .private.start import start
    from .private.menu import menu
    from .private.schedule import schedule
    router = Router()

    router.include_router(start.router)
    router.include_router(menu.router)
    router.include_router(schedule.router)
    router.include_router(group_start)
    router.include_router(group_schedule)

    return router
