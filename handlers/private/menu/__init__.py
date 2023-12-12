from aiogram import Router


def get_menu_router() -> Router:
    from . import menu

    router = Router()
    router.include_router(menu.router)

    return router
