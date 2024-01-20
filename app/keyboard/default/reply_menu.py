from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def menu_reply() -> ReplyKeyboardMarkup:
    """reply keyboard for call main menu"""
    builder = ReplyKeyboardBuilder()
    builder.button(text="ℹ️ Показать меню")
    return builder.as_markup(resize_keyboard=True)
