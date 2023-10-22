
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

        return_data = (False, None)

        # user picked a today button, return schedule for today
        if callback_data.act == "TODAY":
            return_data = True, datetime.today().date()

        # user picked a tomorrow button, return schedule for tomorrow
        if callback_data.act == "TOMORROW":
            tomorrow = datetime.today().date() + timedelta(days=1)
            return_data = True, tomorrow

        # user picked a calendar button, return schedule for day that user choose
        if callback_data.act == "CALENDAR":
            await query.message.edit_reply_markup(reply_markup=await Calendar().start_calendar())

            selected, date = await Calendar().process_selection() # здесь возникает ошибка (нужно разобрать)
            if selected:
                return_data = True, date

        # user picked a MENU button, back to main menu
        if callback_data.act == 'MENU':
            return_data = False, None

        return return_data
