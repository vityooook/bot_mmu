from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from API.request_schedule import request_schedule
from keyboards.inline.calendar_my import Calendar, CaCallback
from keyboards.inline.menu_first_schedule import MenuSchedule, FrScCallback
from keyboards.inline.menu_second_schedule import MenuSecondSchedule, ScScCallback
from keyboards.reply.menu import main_menu
from loader import bot

router = Router()
@router.message(F.text == 'расписание')
async def command_schedule(msg: Message):
    await msg.delete()
    # remove a reply keyboard so as not to interfere
    msg_delete = await msg.answer(text='загрузка', reply_markup=ReplyKeyboardRemove())
    # call a menu with inline keyboard
    await msg.answer(text='выбери', reply_markup=await MenuSchedule().start_menu())
    await bot.delete_message(chat_id=msg_delete.chat.id, message_id=msg_delete.message_id)


@router.callback_query(FrScCallback.filter())
async def process_first_schedule(query: CallbackQuery, callback_data: FrScCallback):
    await query.message.edit_text('загрузка...')
    # catch callback data from menu
    selected, date_for_schedule = await MenuSchedule().process_selection_menu(query=query, callback_data=callback_data)

    if selected == "TODAY" or selected == "TOMORROW":
        data = request_schedule(user_id=query.from_user.id, time_data=date_for_schedule)

        await query.message.edit_text(data,
                                      reply_markup=await MenuSecondSchedule().start_second_menu(date=date_for_schedule))
    elif selected == "CALENDAR":
        await query.message.edit_text(text='выбери точную дату', reply_markup=await Calendar().start_calendar())

    elif selected == "MENU":
        await query.message.delete()
        await query.message.answer('главное меню', reply_markup=main_menu())


@router.callback_query(CaCallback.filter())
async def process_calendar(query: CallbackQuery, callback_data: CaCallback):
    await query.message.edit_text('загрузка...')
    selected, date_for_schedule = await Calendar().process_selection(query=query, callback_data=callback_data)

    if selected:
        data = request_schedule(user_id=query.from_user.id, time_data=date_for_schedule)
        await query.message.edit_text(data,
                                      reply_markup=await MenuSecondSchedule().start_second_menu(date=date_for_schedule))


@router.callback_query(ScScCallback.filter())
async def process_first_schedule(query: CallbackQuery, callback_data: ScScCallback):
    await query.message.edit_text('загрузка...')
    selected, date_for_schedule = await MenuSecondSchedule().process_second_menu(query=query,
                                                                                 callback_data=callback_data)
    if selected:
        data = request_schedule(user_id=query.from_user.id, time_data=date_for_schedule)
        await query.message.edit_text(data,
                                      reply_markup=await MenuSecondSchedule().start_second_menu(date=date_for_schedule))
    else:
        await query.message.delete()
        await query.message.answer('главное меню', reply_markup=main_menu())
