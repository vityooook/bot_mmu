from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from loader import dp


class Form(StatesGroup):
    name_group = State()
    data_lesson = State()


@dp.message(Command("schedule"))
async def command_start(msg: Message, state: FSMContext):
    await state.set_state(Form.name_group)
    await msg.answer("Напищи название твоей группы (пример: экн211-1)")


@dp.message(Form.name_group)
async def process_name_group(msg: Message, state: FSMContext):
    # проверить если такая группа в БД
    await state.update_data(name_group=msg.text)
    # логируй состояние
    await state.set_state(Form.data_lesson)
    await msg.answer('теперь напиши дату (пример: 2023.09.21')

@dp.message(Form.data_lesson)
async def process_data_lesson(msg: Message, state: FSMContext):
    await state.update_data(data_lesson=msg.text)
    await msg.answer('подожди немного')