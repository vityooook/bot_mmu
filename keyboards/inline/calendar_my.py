import calendar
from datetime import datetime, timedelta
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery


class MyCallback(CallbackData, prefix='my_callback'):
    act: str
    year: int
    month: int
    day: int

class Calendar:
    async def start_calendar(
            self,
            year: int = datetime.now().year,
            month: int = datetime.now().month
    ) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        ignore_callback = MyCallback(act="IGNORE", year=year, month=month, day=0)

        # First row - Month and Year name
        month_name: str = calendar.LocaleTextCalendar(locale='ru_RU.UTF-8').formatmonthname(year, month, width=0)
        builder.button(text=f"{month_name}", callback_data=ignore_callback)

        # Second row - Week Days
        for day in ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]:
            builder.button(text=day, callback_data=ignore_callback)

        # Calendar rows - Days of month
        month_calender = calendar.monthcalendar(year, month)
        for week in month_calender:
            for day in week:
                if day == 0:
                    builder.button(text=' ', callback_data=ignore_callback)
                    continue
                builder.button(text=str(day), callback_data=MyCallback(act='DAY', year=year, month=month, day=day))
        # Last row - Buttons
        builder.button(text='<<', callback_data=MyCallback(act='PREV-MONTH', year=year, month=month, day=1))
        builder.button(text='>>', callback_data=MyCallback(act='NEXT-MONTH', year=year, month=month, day=1))
        builder.adjust(1, 7)
        return builder.as_markup()

    async def process_selection(self, query: CallbackQuery, callback_data: MyCallback) -> tuple:
        return_data = (False, None)
        temp_date = datetime(year=callback_data.year, month=callback_data.month, day=1)
        # processing empty buttons, answering with no action
        if callback_data.act == "IGNORE":
            await query.answer(cache_time=60)
        # user picked a day button, return date
        if callback_data.act == "DAY":
            await query.message.delete_reply_markup()  # removing inline keyboard
            await query.message.delete()
            return_data = True, datetime(callback_data.year, callback_data.month, callback_data.day)
        # user navigates to previous month, editing message with new calendar
        if callback_data.act == "PREV-MONTH":
            prev_date = temp_date - timedelta(days=1)
            await query.message.edit_reply_markup(reply_markup=await self.start_calendar(int(prev_date.year),
                                                                                         int(prev_date.month)))
        # user navigates to next month, editing message with new calendar
        if callback_data.act == "NEXT-MONTH":
            next_date = temp_date + timedelta(days=31)
            await query.message.edit_reply_markup(reply_markup=await self.start_calendar(int(next_date.year),
                                                                                         int(next_date.month)))
        return return_data
