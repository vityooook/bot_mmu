from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.state import State, StatesGroup

from data.request_schedule import request_schedule
from keyboards.inline.menu_first_schedule import MenuSchedule, FrScCallback
from keyboards.inline.menu_second_schedule import MenuSecondSchedule, ScScCallback
from keyboards.reply.menu import main_menu
from loader import bot

router = Router()


class DateUser(StatesGroup):
    date = State()


@router.message(F.text == 'расписание')
async def command_schedule(msg: Message):
    await msg.delete()
    msg_delete = await msg.answer(text='загрузка', reply_markup=ReplyKeyboardRemove())
    await msg.answer(text='выбери', reply_markup=await MenuSchedule().start_menu())
    await bot.delete_message(chat_id=msg_delete.chat.id, message_id=msg_delete.message_id)


@router.callback_query(FrScCallback.filter())
async def process_first_schedule(query: CallbackQuery, callback_data: FrScCallback): #здесь ошибка при повторе
    await query.message.edit_text('загрузка...')
    selected, date = await MenuSchedule().process_selection_menu(query=query, callback_data=callback_data)
    if selected:
        time_data = date
        data = request_schedule(user_id=query.from_user.id, time_data=time_data)

        await query.message.edit_text(data, parse_mode=ParseMode.HTML,
                                      reply_markup=await MenuSecondSchedule(time=time_data).start_second_menu())
    else:
        await query.message.delete()
        await query.message.answer('главное меню', reply_markup=main_menu())


@router.callback_query(ScScCallback.filter())
async def process_first_schedule(query: CallbackQuery, callback_data: ScScCallback):
    await query.message.edit_text('загрузка...')
    selected = await MenuSecondSchedule().process_second_menu(query=query, callback_data=callback_data)
    if selected:
        await query.message.delete()
        await query.message.answer('главное меню', reply_markup=main_menu())