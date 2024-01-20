from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import GroupsCallback


def back_to_main_menu() -> InlineKeyboardMarkup:
    """Inline keyboard for back to main menu"""
    builder = InlineKeyboardBuilder()

    builder.button(text="🐈‍⬛ назад", callback_data=GroupsCallback(act="BACK"))

    builder.adjust(1)
    return builder.as_markup()
