from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import RatingBack


def back() -> InlineKeyboardMarkup:
    """Back to rating menu"""
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🐈‍⬛ назад",
        callback_data=RatingBack(act="BACK")
    )
    builder.adjust(1)
    return builder.as_markup()
