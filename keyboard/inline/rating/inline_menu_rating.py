from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import RatingMenuCallback


class InlineMenuRating:
    async def menu(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(text="посмотреть рейтинг",
                       callback_data=RatingMenuCallback(act="SEE-RATING"))

        builder.button(text="оставить отзыв",
                       callback_data=RatingMenuCallback(act="LEAVE-FEEDBACK"))

        builder.button(text="назад",
                       callback_data=RatingMenuCallback(act="BACK"))

        builder.adjust(2, 1)
        return builder.as_markup()
