from aiogram import Router


def get_rating_router() -> Router:
    from . import rating_feedback, rating_call_menu, teacher_rating, list_of_teachers

    router = Router()
    router.include_router(rating_call_menu.router)
    router.include_router(teacher_rating.router)
    router.include_router(rating_feedback.router)
    router.include_router(list_of_teachers.router)

    return router
