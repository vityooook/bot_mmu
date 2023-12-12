from aiogram import Router


def get_siting_router() -> Router:
    from . import siting

    router = Router()
    router.include_router(siting.router)

    return router
