from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import RatingMenuBackCallback


class InlineMenuBackRating:
    async def menu_back(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(text="назад",
                       callback_data=RatingMenuBackCallback(act="BACK"))

        builder.adjust(1)
        return builder.as_markup()
