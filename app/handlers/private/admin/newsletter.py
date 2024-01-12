from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from loguru import logger

from database import crud
from config import ADMIN

router = Router()


class Newsletter(StatesGroup):
    text = State()
    photo = State()


@router.message(Command("newsletter"))
async def cmd_newsletter(msg: Message, state: FSMContext):
    await msg.answer("напишите текст, для рассылки")
    await state.set_state(Newsletter.text)


@router.message(Newsletter.text)
async def process_text(msg: Message, state: FSMContext):
    await state.update_data(text=msg.text)
    await msg.answer("текст принят.\nскиньте фото")
    await state.set_state(Newsletter.photo)


@router.message(Newsletter.photo)
async def process_photo(msg: Message, state: FSMContext):
    await state.update_data(photo=msg.photo)
    data = await state.get_data()
    await state.clear()
    await msg.answer_photo(
        photo=data["photo"],
        caption=data["text"]
    )