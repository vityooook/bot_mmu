from aiogram import Router


def get_groups_router() -> Router:
    from . import groups

    router = Router()
    router.include_router(groups.router)

    return router
