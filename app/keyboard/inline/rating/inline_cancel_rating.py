from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import RatingCancelCallback


class InlineCancelRating:
    async def menu_back(self) -> InlineKeyboardMarkup:
        """Back to main menu"""
        builder = InlineKeyboardBuilder()

        builder.button(
            text="отмена",
            callback_data=RatingCancelCallback(act="CANCEL")
        )

        builder.adjust(1)
        return builder.as_markup()
