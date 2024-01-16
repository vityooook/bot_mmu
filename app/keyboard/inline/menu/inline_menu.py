from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import MenuCallback


class InlineMenu:
    async def menu(self) -> InlineKeyboardMarkup:
        """main menu"""
        builder = InlineKeyboardBuilder()

        builder.button(text="📅 расписание", callback_data=MenuCallback(act="schedule"))

        builder.button(text="👨‍🏫 рейтинг", callback_data=MenuCallback(act="RATING"))

        builder.button(text="⚙️ настройки", callback_data=MenuCallback(act="SITING"))

        builder.button(text="🏘️ группы", callback_data=MenuCallback(act="GROUPS"))

        builder.adjust(1, 1, 2)
        return builder.as_markup()
