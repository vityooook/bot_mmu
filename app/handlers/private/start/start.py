from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from loguru import logger

# * import main menu reply keyboard
from keyboard.default.reply_menu import menu_reply
# * import requests to database
from database import crud


router = Router()


class UserInfo(StatesGroup):
    user_group = State()


@logger.catch()
@router.message(CommandStart())
async def cmd_start_handler(msg: Message, state: FSMContext):
    """Launch a bot

    :param msg: message sent by the user
    :param state: inherit fsm
    """
    logger.info("command /start")
    if await crud.user.verify_id(msg.from_user.id):
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


@logger.catch()
@router.message(UserInfo.user_group)
async def process_user_group(msg: Message, state: FSMContext):
    """Handling the state when the student entered group name

    :param msg: message sent by the user
    :param state: inherit fsm
    """
    # * check if the group exist
    if await crud.group.verify_group(msg.text.upper()):
        # * with the same request we get the group id
        group_id = await crud.group.verify_group(msg.text.upper())
        info = msg.from_user
        # * add information about new student
        await crud.user.add_user_info(
            info.id,
            group_id,
            info.first_name,
            info.last_name,
            info.username
        )
        await msg.answer("спасибо, все супер\nтеперь ты можешь получить расписание",
                         reply_markup=menu_reply())
    else:
        await msg.answer('такой группы нету')

