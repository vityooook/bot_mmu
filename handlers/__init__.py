from aiogram import Router


def get_handlers_router() -> Router:
    from .start import start
    from .menu import menu
    from .schedule import schedule
    router = Router()

    router.include_router(start.router)
    router.include_router(menu.router)
    router.include_router(schedule.router)

    return router
