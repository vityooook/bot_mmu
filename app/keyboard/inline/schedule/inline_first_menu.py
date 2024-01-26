from datetime import datetime, timedelta
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import CallbackQuery

from handlers.callback.callback_data import ScheduleFirstMenuCallback as Callback


class FirstMenuSchedule:
    async def menu(self) -> InlineKeyboardMarkup:
        """Schedule menu"""

        builder = InlineKeyboardBuilder()

        # * First row - this day and next day
        builder.button(text='сегодня', callback_data=Callback(act="TODAY"))
        builder.button(text='завтра', callback_data=Callback(act="TOMORROW"))

        # * Second row - week
        builder.button(text="неделя", callback_data=Callback(act="WEEK"))

        # * Third row - calendar
        builder.button(text='точная дата', callback_data=Callback(act="CALENDAR"))

        # * Last row - back to main menu
        builder.button(text='🐈‍⬛ назад', callback_data=Callback(act="BACK"))

        builder.adjust(2, 1, 1, 1)
        return builder.as_markup()

    async def process_selection_menu(self, callback_data: Callback) -> tuple:

        return_data = (str, None)

        # * user picked a today button, return schedule for today
        if callback_data.act == "TODAY":
            return_data = "TODAY", datetime.today().date()

        # * user picked a tomorrow button, return schedule for tomorrow
        elif callback_data.act == "TOMORROW":
            tomorrow = datetime.today().date() + timedelta(days=1)
            return_data = "TOMORROW", tomorrow

        elif callback_data.act == "WEEK":
            return_data = "WEEK", datetime.today().date()

        # * user picked a calendar button, return schedule for day that user choose
        elif callback_data.act == "CALENDAR":
            return_data = "CALENDAR", None

        # * user picked a MENU button, back to main menu
        elif callback_data.act == 'BACK':
            return_data = 'BACK', None

        return return_data
