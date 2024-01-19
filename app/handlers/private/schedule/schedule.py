from aiogram import Router, F
from aiogram.types import CallbackQuery
from loguru import logger

# * import requests to university's API
from API.request_schedule import get_day_schedule
# * import inline rating menu keyboard
from keyboard.inline.menu.inline_menu import main_menu
# * import callback
from handlers.callback.callback_data import (
    MenuCallback,
    ScheduleCalendarCallback,
    ScheduleFirstMenuCallback,
    ScheduleSecondMenuCallback
)
# * import inline schedule menu keyboard
from keyboard.inline.schedule.inline_first_menu import FirstMenuSchedule
# * import inline keyboard with additional functionality
from keyboard.inline.schedule.inline_second_menu import SecondMenuSchedule
# * import inline keyboard where u can chose date from calendar
from keyboard.inline.schedule.inline_calendar import Calendar

router = Router()


@logger.catch()
@router.callback_query(MenuCallback.filter(F.act == "SCHEDULE"))
async def schedule(query: CallbackQuery):
    """Working out a callback for a call schedule menu

    :param query: this object represents an incoming callback query from a callback button
    """
    logger.info("Schedule menu is called")
    await query.message.edit_text(
        text="<b>меню расписания:</b>",
        reply_markup=await FirstMenuSchedule().menu()
    )


@logger.catch()
@router.callback_query(ScheduleFirstMenuCallback.filter())
async def process_first_schedule(
        query: CallbackQuery,
        callback_data: ScheduleFirstMenuCallback
):
    """Working out a callback to understand what day he wants to receive a schedule

    :param query: this object represents an incoming callback query from a callback button
    :param callback_data: the callback with some information
    """
    await query.message.edit_text("мур мур...")
    selected, date_for_schedule = await FirstMenuSchedule().process_selection_menu(
        callback_data=callback_data
    )
    # * get the data from the callback and perform the actions
    if selected == "TODAY" or selected == "TOMORROW":
        data = await get_day_schedule(user_id=query.from_user.id, date=date_for_schedule)
        await query.message.edit_text(
            data,
            reply_markup=await SecondMenuSchedule().menu(date=date_for_schedule)
        )
    elif selected == "CALENDAR":
        await query.message.edit_text(
            text="выбери дату:",
            reply_markup=await Calendar().start_calendar()
        )

    elif selected == "BACK":
        await query.message.edit_text(
            "МЯУ бот создан для студентов.\n\n<b>Выберите нужное действие:</b>",
            reply_markup=main_menu()
        )


@logger.catch()
@router.callback_query(ScheduleCalendarCallback.filter())
async def process_calendar(query: CallbackQuery, callback_data: ScheduleCalendarCallback):
    """Working out a callback to get calendar for user

    :param query: this object represents an incoming callback query from a callback button
    :param callback_data: the callback with some information
    """
    await query.message.edit_text("мур мур...")
    selected, date_for_schedule = await Calendar().process_selection(
        query=query,
        callback_data=callback_data
    )
    if selected:
        data = await get_day_schedule(user_id=query.from_user.id, date=date_for_schedule)
        await query.message.edit_text(
            data,
            reply_markup=await SecondMenuSchedule().menu(date=date_for_schedule)
        )


@logger.catch()
@router.callback_query(ScheduleSecondMenuCallback.filter())
async def process_second_schedule(
        query: CallbackQuery,
        callback_data: ScheduleSecondMenuCallback
):
    """The user has already received the schedule and can return to the main menu or
    view the schedule for the next day

    :param query: this object represents an incoming callback query from a callback button
    :param callback_data: the callback with some information
    """
    await query.message.edit_text("мур мур...")
    selected, date_for_schedule = await SecondMenuSchedule().process_selection_menu(
        query=query,
        callback_data=callback_data
    )
    if selected:
        data = await get_day_schedule(user_id=query.from_user.id, date=date_for_schedule)
        await query.message.edit_text(
            data,
            reply_markup=await SecondMenuSchedule().menu(date=date_for_schedule)
        )
    else:
        await query.message.edit_text(
            text="<b>меню расписания:</b>",
            reply_markup=await FirstMenuSchedule().menu()
        )
