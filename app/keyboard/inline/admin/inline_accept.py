from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import AdminAcceptCallback


class InlineAdminAccept:
    async def accept_newsletter(self) -> InlineKeyboardMarkup:
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
