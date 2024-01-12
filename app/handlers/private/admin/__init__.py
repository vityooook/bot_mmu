from aiogram import Router


def get_admin_router() -> Router:
    from . import newsletter

    router = Router()
    router.include_router(newsletter.router)

    return router
