from aiogram import Router


def get_handlers_router() -> Router:
    # * import functions with routers
    from .private.start import get_start_router
    from .private.menu import get_menu_router
    from .private.rating import get_rating_router
    from .private.schedule import get_schedule_router
    from .private.groups import get_groups_router
    from .private.siting import get_siting_router
    from .private.admin import get_admin_router

    # * a boss router
    router = Router()

    # * made for beauty
    start_router = get_start_router()
    menu_router = get_menu_router()
    rating_router = get_rating_router()
    schedule_router = get_schedule_router()
    groups_router = get_groups_router()
    siting_router = get_siting_router()
    admin_router = get_admin_router()

    # * add all routers at the boss router
    router.include_router(start_router)
    router.include_router(menu_router)
    router.include_router(rating_router)
    router.include_router(schedule_router)
    router.include_router(groups_router)
    router.include_router(siting_router)
    router.include_router(admin_router)

    return router


# def get_handlers_router() -> Router:
#     from .groups.start import router as group_start
#     from .groups.schedule import router as group_schedule
#     from .private.start import start
#     from .private.menu import menu
#     from .private.schedule import schedule
#     from .private.rating import rating_call_menu
#     from .private.rating import teacher_rating
#     from .private.rating import rating_feedback
#     from .private.siting import siting
#     from .private.groups import groups
#     router = Router()
#
#     router.include_router(start.router)
#     router.include_router(menu.router)
#     router.include_router(schedule.router)
#     router.include_router(group_start)
#     router.include_router(group_schedule)
#     router.include_router(rating_call_menu.router)
#     router.include_router(teacher_rating.router)
#     router.include_router(rating_feedback.router)
#     router.include_router(siting.router)
#     router.include_router(groups.router)
#
#     return router
