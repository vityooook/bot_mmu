from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from utils.callback_data import TeacherMenuCallback


class InlineMenuTeacher:
    async def menu(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(text="посмотреть рейтинг",
                       callback_data=TeacherMenuCallback(act="SEE-RATING"))

        builder.button(text="оставить отзыв",
                       callback_data=TeacherMenuCallback(act="LEAVE-FEEDBACK"))

        builder.button(text="назад",
                       callback_data=TeacherMenuCallback(act="BACK"))

        builder.adjust(1, 1, 1)
        return builder.as_markup()
