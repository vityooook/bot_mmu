from aiogram import Router


def get_handlers_router() -> Router:
    from .groups.start import router as group_start
    from .groups.schedule import router as group_schedule
    from .private.start import start
    from .private.menu import menu
    from .private.schedule import schedule
    from .private.rating import rating_call_menu
    from .private.rating import teacher_rating
    from .private.rating import rating_feedback
    router = Router()

    router.include_router(start.router)
    router.include_router(menu.router)
    router.include_router(schedule.router)
    router.include_router(group_start)
    router.include_router(group_schedule)
    router.include_router(teacher_rating.router)
    router.include_router(rating_call_menu.router)
    router.include_router(rating_feedback.router)

    return router
