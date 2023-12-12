import datetime

from aiogram.filters.callback_data import CallbackData

# здесь находятся callback для inline


class MenuCallback(CallbackData, prefix="menu"):
    act: str


class ScheduleCalendarCallback(CallbackData, prefix="schedule_calendar"):
    act: str
    year: int
    month: int
    day: int


class ScheduleFirstMenuCallback(CallbackData, prefix="schedule_first"):
    act: str


class ScheduleSecondMenuCallback(CallbackData, prefix="schedule_second"):
    act: str
    date: datetime.date | None=None


class RatingMenuCallback(CallbackData, prefix="rating_menu"):
    act: str


class RatingMenuBackCallback(CallbackData, prefix="rating_back"):
    act: str


class RatingCancelCallback(CallbackData, prefix="rating_cancel"):
    act: str


class RatingFeedbackCallback(CallbackData, prefix="rating_feedback"):
    act: int
    question: int


class RatingLinkFeedbackCallback(CallbackData, prefix="rating_link_feedback"):
    act: str
    teacher_id: int


class SitingCallback(CallbackData, prefix="siting"):
    act: str


class GroupsCallback(CallbackData, prefix="groups"):
    act: str
