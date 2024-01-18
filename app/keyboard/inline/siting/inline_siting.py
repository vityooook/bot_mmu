from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import SitingCallback


class InlineSiting:
    async def siting_menu(self) -> InlineKeyboardMarkup:
        """Siting menu with two button (change group, back)

        """
        builder = InlineKeyboardBuilder()

        builder.button(text="сменить группу", callback_data=SitingCallback(act="CHANGE-GROUP"))

        builder.button(text="назад", callback_data=SitingCallback(act="BACK"))

        builder.adjust(1, 1)
        return builder.as_markup()