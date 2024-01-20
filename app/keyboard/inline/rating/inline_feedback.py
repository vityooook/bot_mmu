from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import CallbackQuery

from handlers.callback.callback_data import RatingFeedbackCallback as Callback


def start_feedback(question: int = 1) -> InlineKeyboardMarkup:
    """Buttons for rating teachers from 1 to 5"""
    builder = InlineKeyboardBuilder()

    builder.button(text="1", callback_data=Callback(act=1, question=question))
    builder.button(text="2", callback_data=Callback(act=2, question=question))
    builder.button(text="3", callback_data=Callback(act=3, question=question))
    builder.button(text="4", callback_data=Callback(act=4, question=question))
    builder.button(text="5", callback_data=Callback(act=5, question=question))

    builder.adjust(5)
    return builder.as_markup()
