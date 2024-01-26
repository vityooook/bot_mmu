from datetime import timedelta
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from handlers.callback.callback_data import ScheduleWeekMenuCallback as Callback


class WeekMenu:
    async def menu(self, date) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        # First row - previous day or next day
        builder.button(text="⬅️", callback_data=Callback(act="PREVIOUS-WEEK", date=date))
        builder.button(text="➡️", callback_data=Callback(act="NEXT-WEEK", date=date))
        builder.button(text="🐈‍⬛ назад️", callback_data=Callback(act="BACK"))

        # Second row - main menu
        builder.adjust(2)
        return builder.as_markup()

    async def process_selection_menu(self, callback_data: Callback) -> tuple:
        return_data = False, None
        date = callback_data.date

        if callback_data.act == "PREVIOUS-WEEK":
            previous = date - timedelta(days=7)
            callback_data.date = previous
            return_data = True, previous

        elif callback_data.act == "NEXT-WEEK":
            next = date + timedelta(days=7)
            callback_data.date = next
            return_data = True, next

        elif callback_data.act == "BACK":
            return_data = False, None

        return return_data

