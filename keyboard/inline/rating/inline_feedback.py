from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import CallbackQuery

from handlers.callback.callback_data import RatingFeedbackCallback as Callback


class InlineFeedback:

    async def start_feedback(
            self,
            question: int = 1,
    ) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(text="1", callback_data=Callback(act=1, question=question))
        builder.button(text="2", callback_data=Callback(act=2, question=question))
        builder.button(text="3", callback_data=Callback(act=3, question=question))
        builder.button(text="4", callback_data=Callback(act=4, question=question))
        builder.button(text="5", callback_data=Callback(act=5, question=question))

        builder.adjust(5)
        return builder.as_markup()

    async def process_selection(
            self,
            query: CallbackQuery,
            callback_data: Callback
    ) -> dict:
        return_data = {
            "select": False,
            "mark": int,
            "question": int
        }

        if callback_data.act == 1:
            return_data["select"] = True
            return_data["mark"] = callback_data.act
            return_data["question"] = callback_data.question

        elif callback_data.act == 2:
            return_data["select"] = True
            return_data["mark"] = callback_data.act
            return_data["question"] = callback_data.question

        elif callback_data.act == 3:
            return_data["select"] = True
            return_data["mark"] = callback_data.act
            return_data["question"] = callback_data.question

        elif callback_data.act == 4:
            return_data["select"] = True
            return_data["mark"] = callback_data.act
            return_data["question"] = callback_data.question

        elif callback_data.act == 5:
            return_data["select"] = True
            return_data["mark"] = callback_data.act
            return_data["question"] = callback_data.question

        return return_data
