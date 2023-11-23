
from datetime import datetime, timedelta
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery

from keyboards.inline.calendar_my import Calendar


class FrScCallback(CallbackData, prefix='first'):      # поработать с названием
    act: str


class MenuSchedule:
    async def start_menu(self) -> InlineKeyboardMarkup:

        builder = InlineKeyboardBuilder()

        # First row - this day and next day
        builder.button(text='сегодня', callback_data=FrScCallback(act="TODAY"))
        builder.button(text='завтра', callback_data=FrScCallback(act="TOMORROW"))

        # Second row - calendar
        builder.button(text='точная дата', callback_data=FrScCallback(act="CALENDAR"))

        # Last row - back to main menu
        builder.button(text='меню', callback_data=FrScCallback(act="MENU"))

        builder.adjust(2, 1, 1)
        return builder.as_markup()

    async def process_selection_menu(self, query: CallbackQuery, callback_data: FrScCallback) -> tuple:

        return_data = (str, None)

        # user picked a today button, return schedule for today
        if callback_data.act == "TODAY":
            return_data = "TODAY", datetime.today().date()

        # user picked a tomorrow button, return schedule for tomorrow
        elif callback_data.act == "TOMORROW":
            tomorrow = datetime.today().date() + timedelta(days=1)
            return_data = "TOMORROW", tomorrow

        # user picked a calendar button, return schedule for day that user choose
        elif callback_data.act == "CALENDAR":
            return_data = "CALENDAR", None

        # user picked a MENU button, back to main menu
        elif callback_data.act == 'MENU':
            return_data = 'MENU', None

        return return_data
