from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import RatingMenuCallback


def rating_menu() -> InlineKeyboardMarkup:
    """Rating menu with three buttons (see rating, leave feedback, back)"""
    builder = InlineKeyboardBuilder()

    builder.button(
        text="👀 рейтинг",
        callback_data=RatingMenuCallback(act="SEE-RATING")
    )

    builder.button(
        text="✍️ отзыв",
        callback_data=RatingMenuCallback(act="LEAVE-FEEDBACK")
    )

    builder.button(
        text="список преподавателей",
        callback_data=RatingMenuCallback(act="LIST_OF_TEACHERS")
    )

    builder.button(
        text="🐈‍⬛ назад",
        callback_data=RatingMenuCallback(act="BACK")
    )

    builder.adjust(2, 1)
    return builder.as_markup()
