from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import RatingLinkFeedbackCallback


def leavefeedback_or_back(teacher_id: int) -> InlineKeyboardMarkup:
    """When a student sees a teacher's rating,
    he/she can return to the main menu or leave a review."""
    builder = InlineKeyboardBuilder()

    builder.button(
        text="✍️ отзыв",
        callback_data=RatingLinkFeedbackCallback(
            act="LINK",
            teacher_id=f"{teacher_id}"
        )
    )
    builder.button(
        text="🐈‍⬛ назад",
        callback_data=RatingLinkFeedbackCallback(
            act="BACK",
            teacher_id=0
        )
    )
    builder.adjust(1)
    return builder.as_markup()
