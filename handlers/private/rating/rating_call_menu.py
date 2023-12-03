from aiogram import Router, F
from aiogram.types import CallbackQuery

from handlers.callback.callback_data import MenuCallback, RatingMenuCallback
from keyboard.inline.rating.inline_menu_rating import InlineMenuRating
from keyboard.inline.menu.inline_menu import InlineMenu


router = Router()


@router.callback_query(MenuCallback.filter(F.act == "RATING"))
async def teacher_rating(query: CallbackQuery):
    await query.message.edit_text(
        text="меню рейтинга преподователей:",
        reply_markup=await InlineMenuRating().menu()
    )


@router.callback_query(RatingMenuCallback.filter((F.act == "BACK")))
async def back_to_main_menu(query: CallbackQuery):
    await query.message.edit_text(
        "МЯУ бот создан для студентов.\n\n<b>Выберите нужное действие:</b>",
        reply_markup=await InlineMenu().menu()
    )
