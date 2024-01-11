from aiogram import Router


def get_start_router() -> Router:
    from . import start

    router = Router()
    router.include_router(start.router)

    return router
