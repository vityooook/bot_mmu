from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import MenuCallback


class InlineMenu:
    async def menu(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(text="📅 расписание", callback_data=MenuCallback(act="schedule"))

        builder.button(text="👨‍🏫 рейтинг", callback_data=MenuCallback(act="teacher_rating"))

        builder.button(text="⚙️ настройки", callback_data=MenuCallback(act="settings"))

        builder.button(text="🏘️ группы", callback_data=MenuCallback(act="groups"))

        builder.adjust(1, 1, 2)
        return builder.as_markup()