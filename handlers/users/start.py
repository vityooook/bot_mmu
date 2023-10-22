from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.reply.menu import main_menu
from data import db

router = Router()


class Userinfo(StatesGroup):
    user_group = State()


@router.message(CommandStart())
async def cmd_start_handler(msg: Message, state: FSMContext):
    await msg.delete()
    if db.id_check(msg.from_user.id):
        await msg.answer(f"Приветик,{msg.from_user.username}, давно не виделись", reply_markup=main_menu())
    else:
        await msg.answer('Приветик, это бот от университета МЯУ, который может скинуть расписание!')
        await state.set_state(Userinfo.user_group)
        await msg.answer("Напищи название твоей группы (пример: ЭКН11-1)")


@router.message(Userinfo.user_group)
async def process_user_group(msg: Message, state: FSMContext):
    if db.check_group_by_name(msg.text.upper()):
        await state.update_data(user_group=msg.text.upper())
        user_group = await state.get_data()
        user_id = msg.from_user.id
        db.add_info_user(user_id, user_group['user_group'])
        await msg.answer("спасибо, все супер\n теперь ты можешь получить расписание")
        await state.clear()
    else:
        await msg.answer('такой группы нету')

