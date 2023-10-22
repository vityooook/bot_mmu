
from datetime import datetime, timedelta, date
from typing import Optional

from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery

from data.request_schedule import request_schedule


class ScScCallback(CallbackData, prefix='second'):      # поработать с названием
    act: str


class MenuSecondSchedule:

    def __init__(self, time: datetime):
        self.time = time

    async def start_second_menu(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        # First row - previous day or next day
        builder.button(text="U+2B05", callback_data=ScScCallback(act="PREVIOUS"))
        builder.button(text="U+27A1", callback_data=ScScCallback(act="NEXT"))

        # Second row - main menu
        builder.button(text="меню", callback_data=ScScCallback(act="MENU"))

        builder.adjust(2, 1)
        return builder.as_markup()

    async def process_second_menu(self, query: CallbackQuery, callback_data: ScScCallback):
        return_data = False

        if callback_data.act == "PREVIOUS":
            previous = self.time - timedelta(days=1)
            text = request_schedule(user_id=query.from_user.id, time_data=previous)
            await query.message.edit_text(text=text)

        if callback_data.act == "NEXT":
            next = self.time + timedelta(days=1)
            text = request_schedule(user_id=query.from_user.id, time_data=next)
            await query.message.edit_text(text=text)

        if callback_data.act == "MENU":
            return_data = True

        return return_data

