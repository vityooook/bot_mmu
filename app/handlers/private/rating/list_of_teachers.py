from aiogram import Router, F
from aiogram.types import CallbackQuery
from loguru import logger

# * # * import requests to university's API
from API.request_schedule import get_teachers_name
# * import callback
from handlers.callback.callback_data import RatingMenuCallback
# * import inline rating menu keyboard
from keyboard.inline.rating.back_to_rating_menu import back


router = Router()


@logger.catch()
@router.callback_query(RatingMenuCallback.filter(F.act == "LIST_OF_TEACHERS"))
async def student_teachers(query: CallbackQuery):
    name = await get_teachers_name(query.from_user.id)
    await query.message.edit_text(
        "Вот список преподавателей на текущий семестр:\n"
        f"{name}"
        "<i>\n\nМяу, возможны некоторые несоответствия, так как я не знаю твою группу по английскому.</i>",
        reply_markup=back()
    )
