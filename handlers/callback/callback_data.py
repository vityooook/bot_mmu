import datetime

from aiogram.filters.callback_data import CallbackData


class MenuCallback(CallbackData, prefix='menu'):
    act: str


class ScheduleCalendarCallback(CallbackData, prefix='schedule_calendar'):
    act: str
    year: int
    month: int
    day: int


class ScheduleFirstMenuCallback(CallbackData, prefix='schedule_first'):
    act: str


class ScheduleSecondMenuCallback(CallbackData, prefix='schedule_second'):
    act: str
    date: datetime.date | None=None
