from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def main_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="расписание")
    builder.button(text='инфа')
    return builder.as_markup(resize_keyboard=True)
