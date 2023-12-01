from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from utils.callback_data import TeacherMenuCallback
from keyboard.inline.teacher.inline_menu_back_teacher import InlineMenuBackTeacher

router = Router()


class TeacherName(StatesGroup):
    teacher_name = State()


@router.callback_query(TeacherMenuCallback.filter(F.act == "SEE-RATING"))
async def see_rating(query: CallbackQuery, state: FSMContext):
    await query.message.answer(
        "напиши фио преподователя",
        reply_markup=await InlineMenuBackTeacher().menu_back())
    await state.set_state(TeacherName.teacher_name)

@router.message(TeacherName.teacher_name)
async def process_selecting_teacher(msg: Message, state: FSMContext):
    pass
        #нужно сделать обращение к бд с преподами
