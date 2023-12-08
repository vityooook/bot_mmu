from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import RatingLinkFeedbackCallback


class InlineLinkBackRating:
    async def link_back(self, teacher_id: int) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(
            text="оставить отзыв",
            callback_data=RatingLinkFeedbackCallback(
                act="LINK",
                teacher_id=f"{teacher_id}"
            )
        )
        builder.button(
            text="назад",
            callback_data=RatingLinkFeedbackCallback(
                act="BACK",
                teacher_id=None
            )
        )
        builder.adjust(1)
        return builder.as_markup()