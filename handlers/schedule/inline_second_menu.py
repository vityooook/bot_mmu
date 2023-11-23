from datetime import datetime, timedelta
import datetime as add
from typing import Optional

from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery


class ScScCallback(CallbackData, prefix='second'):
    act: str
    date: timedelta | None


class MenuSecondSchedule:

    async def start_second_menu(self, date: add.date) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        # First row - previous day or next day
        builder.button(text="⬅️", callback_data=ScScCallback(act="PREVIOUS", date=date))
        builder.button(text='сегодня', callback_data=ScScCallback(act="TODAY"))
        builder.button(text="➡️", callback_data=ScScCallback(act="NEXT", date=date))

        # Second row - main menu
        builder.button(text="меню", callback_data=ScScCallback(act="MENU"))

        builder.adjust(3, 1)
        return builder.as_markup()

    async def process_second_menu(self, query: CallbackQuery, callback_data: ScScCallback) -> tuple:
        return_data = False, None
        date = callback_data.date

        if callback_data.act == "PREVIOUS":
            previous = date - timedelta(days=1)
            callback_data.date = previous
            return_data = True, previous

        elif callback_data.act == "TODAY":
            today = datetime.today().date()
            callback_data.date = today
            return_data = True, today

        elif callback_data.act == "NEXT":
            next = date + timedelta(days=1)
            callback_data.date = next
            return_data = True, next

        elif callback_data.act == "MENU":
            return_data = False, None

        return return_data

