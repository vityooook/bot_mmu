from aiogram import Router, F
from aiogram.types import CallbackQuery
from loguru import logger

from handlers.callback.callback_data import (
    MenuCallback,
    RatingMenuCallback,
    RatingLinkFeedbackCallback,
    RatingBack
)
# * import inline rating menu keyboard
from keyboard.inline.rating.inline_menu_rating import rating_menu
# * import inline group menu keyboard
from keyboard.inline.menu.inline_menu import main_menu
router = Router()


@logger.catch()
@router.callback_query(MenuCallback.filter(F.act == "RATING"))
@router.callback_query(RatingBack.filter(F.act == "BACK"))
@router.callback_query(RatingLinkFeedbackCallback.filter(F.act == "BACK"))
async def teacher_rating(query: CallbackQuery):
    """Working out a callback for a call rating menu

    :param query: this object represents an incoming callback query from a callback button
    """
    logger.debug("Ratings menu is called up")
    await query.message.edit_text(
        "🌟 <b>Рейтинг преподавателей</b> 🌟",
        reply_markup=rating_menu()
    )


@logger.catch()
@router.callback_query(RatingMenuCallback.filter(F.act == "BACK"))
async def back_to_main_menu(query: CallbackQuery):
    """Working out a callback for back to main menu

    :param query: this object represents an incoming callback query from a callback button
    """
    await query.message.edit_text(
        "Мяу-мяу-мяу😻"
        "\n\n<b>меню расписания:</b>",
        reply_markup=main_menu()
    )
