from datetime import datetime, timedelta
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import CallbackQuery

from handlers.callback.callback_data import ScheduleSecondMenuCallback as Callback


class SecondMenuSchedule:
    async def menu(self, date) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        # First row - previous day or next day
        builder.button(text="⬅️", callback_data=Callback(act="PREVIOUS", date=date))
        builder.button(text='сегодня', callback_data=Callback(act="TODAY"))
        builder.button(text="➡️", callback_data=Callback(act="NEXT", date=date))
        builder.button(text="🐈‍⬛ назад️", callback_data=Callback(act="BACK"))

        # Second row - main menu
        builder.adjust(3)
        return builder.as_markup()

    async def process_selection_menu(self, callback_data: Callback) -> tuple:
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

        elif callback_data.act == "BACK":
            return_data = False, None

        return return_data

