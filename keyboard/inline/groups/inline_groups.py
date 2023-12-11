from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import GroupsCallback


class InlineGroups:
    async def groups_menu(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(text="🐈‍⬛ назад", callback_data=GroupsCallback(act="BACK"))

        builder.adjust(1)
        return builder.as_markup()
