from aiogram import Router


def get_admin_router() -> Router:
    # * import the file.py
    from . import newsletter

    router = Router()
    # * add a router at the main router
    router.include_router(newsletter.router)

    return router
