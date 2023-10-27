
from datetime import datetime, timedelta, date
from typing import Optional

from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery

from data.request_schedule import request_schedule


class ScScCallback(CallbackData, prefix='second'):      # поработать с названием
    act: str


class MenuSecondSchedule:

    # def __init__(self, time: datetime | None):
    #     self.time = time

    async def start_second_menu(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        # First row - previous day or next day
        builder.button(text="⬅️", callback_data=ScScCallback(act="PREVIOUS"))
        builder.button(text='сегодня', callback_data=ScScCallback(act="TODAY"))
        builder.button(text="➡️", callback_data=ScScCallback(act="NEXT"))

        # Second row - main menu
        builder.button(text="меню", callback_data=ScScCallback(act="MENU"))

        builder.adjust(3, 1)
        return builder.as_markup()

    async def process_second_menu(self, query: CallbackQuery, callback_data: ScScCallback, time: datetime) -> tuple:
        return_data = False, None

        if callback_data.act == "PREVIOUS":
            previous = time - timedelta(days=1)
            return_data = True, previous

        elif callback_data.act == "TODAY":
            today = datetime.today().date()
            return_data = True, today

        elif callback_data.act == "NEXT":
            next = time + timedelta(days=1)
            return_data = True, next

        elif callback_data.act == "MENU":
            return_data = False, None

        return return_data

