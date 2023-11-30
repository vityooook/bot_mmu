from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from utils.callback_data import TeacherMenuBackCallback


class InlineMenuBackTeacher:
    async def menu_back(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(text="назад",
                       callback_data=TeacherMenuBackCallback(act="BACK"))

        builder.adjust(1)
        return builder.as_markup()