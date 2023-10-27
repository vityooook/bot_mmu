from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from data.request_schedule import request_schedule
from keyboards.inline2.calendar_my import Calendar, CaCallback
from keyboards.inline2.menu_first_schedule import MenuSchedule, FrScCallback
from keyboards.inline2.menu_second_schedule import MenuSecondSchedule, ScScCallback
from keyboards.reply.menu import main_menu
from loader import bot

router = Router()


class DateUser(StatesGroup):
    date = State()


@router.message(F.text == 'расписание')
async def command_schedule(msg: Message):
    await msg.delete()
    # remove a reply keyboard so as not to interfere
    msg_delete = await msg.answer(text='загрузка', reply_markup=ReplyKeyboardRemove())
    # call a menu with inline keyboard
    await msg.answer(text='выбери', reply_markup=await MenuSchedule().start_menu())
    await bot.delete_message(chat_id=msg_delete.chat.id, message_id=msg_delete.message_id)


@router.callback_query(FrScCallback.filter())
async def process_first_schedule(query: CallbackQuery, callback_data: FrScCallback, state: FSMContext):
    await query.message.edit_text('загрузка...')
    # catch callback data from menu
    selected, date_for_schedule = await MenuSchedule().process_selection_menu(query=query, callback_data=callback_data)

    if selected == "TODAY" or selected == "TOMORROW":
        data = request_schedule(user_id=query.from_user.id, time_data=date_for_schedule)
        # change current state
        await state.set_state(DateUser.date)
        # write new info in user state
        await state.update_data(date=date_for_schedule)
        # call second menu with inline keyboard
        await query.message.edit_text(data,
                                      reply_markup=await MenuSecondSchedule().start_second_menu())
    elif selected == "CALENDAR":
        await query.message.edit_text(text='выбери точную дату', reply_markup=await Calendar().start_calendar())

    elif selected == "MENU":
        await query.message.delete()
        await query.message.answer('главное меню', reply_markup=main_menu())


@router.callback_query(CaCallback.filter())
async def process_calendar(query: CallbackQuery, callback_data: CaCallback, state: FSMContext):
    await query.message.edit_text('загрузка...')
    selected, date_for_schedule = await Calendar().process_selection(query=query, callback_data=callback_data)
    if selected:
        data = request_schedule(user_id=query.from_user.id, time_data=date_for_schedule)
        # change current state
        await state.set_state(DateUser.date)
        # write new info in user state
        await state.update_data(date=date_for_schedule)
        # call second menu with inline keyboard
        await query.message.edit_text(data,
                                      reply_markup=await MenuSecondSchedule().start_second_menu())


@router.callback_query(ScScCallback.filter(), DateUser.date)
async def process_first_schedule(query: CallbackQuery, callback_data: ScScCallback, state: FSMContext):
    await query.message.edit_text('загрузка...')
    date = await state.get_data()
    selected, date_for_schedule = await MenuSecondSchedule()\
        .process_second_menu(query=query,callback_data=callback_data, time=date['date'])
    if selected:
        data = request_schedule(user_id=query.from_user.id, time_data=date_for_schedule)
        await query.message.edit_text(data, reply_markup=await MenuSecondSchedule().start_second_menu())
    else:
        await query.message.delete()
        await query.message.answer('главное меню', reply_markup=main_menu())