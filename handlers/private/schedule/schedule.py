from aiogram import Router, F
from aiogram.types import CallbackQuery

from API.request_schedule import request_schedule
from keyboard.inline.menu.inline_menu import InlineMenu
from handlers.callback.callback_data import (
    MenuCallback,
    ScheduleCalendarCallback,
    ScheduleFirstMenuCallback,
    ScheduleSecondMenuCallback
)
from keyboard.inline.schedule.inline_first_menu import FirstMenuSchedule
from keyboard.inline.schedule.inline_second_menu import SecondMenuSchedule
from keyboard.inline.schedule.inline_calendar import Calendar


router = Router()


@router.callback_query(MenuCallback.filter(F.act == "schedule"))
async def schedule(
        query: CallbackQuery,
):
    # call a menu with inline keyboard
    await query.message.edit_text(text="<b>меню расписания:</b>",
                                  reply_markup=await FirstMenuSchedule().menu()
                                  )


@router.callback_query(ScheduleFirstMenuCallback.filter())
async def process_first_schedule(
        query: CallbackQuery,
        callback_data: ScheduleFirstMenuCallback
):
    await query.message.edit_text("мур мур...")
    # catch callback data from menu
    selected, date_for_schedule = await FirstMenuSchedule().process_selection_menu(
        query=query,
        callback_data=callback_data
    )

    if selected == "TODAY" or selected == "TOMORROW":
        data = request_schedule(
            user_id=query.from_user.id, time_data=date_for_schedule)
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
            reply_markup=await InlineMenu().menu()
        )


@router.callback_query(ScheduleCalendarCallback.filter())
async def process_calendar(query: CallbackQuery, callback_data: ScheduleCalendarCallback):
    await query.message.edit_text("мур мур...")
    selected, date_for_schedule = await Calendar().process_selection(
        query=query,
        callback_data=callback_data
    )
    if selected:
        data = request_schedule(
            user_id=query.from_user.id, time_data=date_for_schedule)
        await query.message.edit_text(
            data,
            reply_markup=await SecondMenuSchedule().menu(date=date_for_schedule)
        )


@router.callback_query(ScheduleSecondMenuCallback.filter())
async def process_second_schedule(
        query: CallbackQuery,
        callback_data: ScheduleSecondMenuCallback
):
    await query.message.edit_text("мур мур...")
    selected, date_for_schedule = await SecondMenuSchedule().process_selection_menu(
        query=query,
        callback_data=callback_data
    )
    if selected:
        data = request_schedule(
            user_id=query.from_user.id, time_data=date_for_schedule)
        await query.message.edit_text(
            data,
            reply_markup=await SecondMenuSchedule().menu(date=date_for_schedule)
        )
    else:
        await query.message.edit_text(
            text="<b>меню расписания:</b>",
            reply_markup=await FirstMenuSchedule().menu()
        )
