from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboard.default.reply_menu import menu_reply
from database import crud
from utils.filters import ChatTypeFilter

router = Router()


class UserInfo(StatesGroup):
    user_group = State()


@router.message(CommandStart(), ChatTypeFilter("private"))
async def cmd_start_handler(msg: Message, state: FSMContext):
    if crud.user.verify_id(msg.from_user.id):
        await msg.answer(
            f"Приветик,{msg.from_user.first_name}, давно не виделись",
            reply_markup=menu_reply()
        )
    else:
        await msg.answer(
            "Приветик, это бот от университета МЯУ, который может скинуть расписание!"
        )
        await state.set_state(UserInfo.user_group)
        await msg.answer("Напищи название твоей группы (пример: ЭКН11-1)")


@router.message(UserInfo.user_group)
async def process_user_group(msg: Message, state: FSMContext):
    if crud.group.verify_group(msg.text.upper()):
        await state.clear()
        group_id = crud.group.verify_group(msg.text.upper())
        info = msg.from_user
        crud.user.add_user_info(info.id, group_id,
                                info.first_name, info.last_name,
                                info.username)
        await msg.answer("спасибо, все супер\nтеперь ты можешь получить расписание",
                         reply_markup=menu_reply())
        await state.clear()
    else:
        await msg.answer('такой группы нету')

