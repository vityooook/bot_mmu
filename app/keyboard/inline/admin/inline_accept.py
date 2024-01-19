from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import AdminAcceptCallback


def accept_newsletter() -> InlineKeyboardMarkup:
    """inline keyboard for accepting or declining newsletter"""
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Потверждаю",
        callback_data=AdminAcceptCallback(act="ACCEPT")
    )
    builder.button(
        text="Отмена",
        callback_data=AdminAcceptCallback(act="DECLINE")
    )
    builder.adjust(1, 1)
    return builder.as_markup()
