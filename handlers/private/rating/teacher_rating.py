from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboard.inline.rating.inline_menu_rating import InlineMenuRating
from keyboard.inline.rating.inline_cancel_rating import InlineCancelRating
from handlers.callback.callback_data import RatingMenuCallback, RatingCancelCallback
from database import crud

router = Router()


class Teacher(StatesGroup):
    name = State()


@router.callback_query(RatingMenuCallback.filter(F.act == "SEE-RATING"))
async def see_rating(query: CallbackQuery, state: FSMContext):
    await query.message.edit_text(
        "напиши фио преподователя",
        reply_markup=await InlineCancelRating().menu_back()
    )
    await state.set_state(Teacher.name)


@router.message(Teacher.name)
async def process_selecting_teacher(msg: Message, state: FSMContext):
    if crud.rating.verify_teacher(msg.text.title()):
        await state.clear()
        teacher_id = crud.rating.verify_teacher(msg.text.title())
        name = msg.text.title()
        rating = crud.rating.get_rating(teacher_id)
        rating_avg = crud.rating.get_avg_rating(teacher_id)
        if rating:
            await msg.answer(
                f"<b>{name}</b>\n\n<b>Средний балл:</b>{rating_avg}"
                f"\n<b>Чувство юмора:</b> {rating[0][1]}"
                f"\n<b>Объективность:</b> {rating[1][1]}"
                f"\n<b>Требовательность:</b> {rating[2][1]}"
                f"\n<b>Изложение материала:</b> {rating[3][1]}"
                f"\n<b>Организованность:</b> {rating[4][1]}"
            )
        else:
            await msg.answer(f"<b>{name}</b>\n\nРейтинг осутствует")
    else:
        await msg.answer(
            "имя фио преподователя не верное",
            reply_markup=await InlineCancelRating().menu_back()
        )


@router.callback_query(RatingCancelCallback.filter(F.act == "CANCEL"))
async def cancel_see_rating(query: CallbackQuery, state: FSMContext):
    await state.clear()
    await query.message.answer(
        text="меню рейтинга преподователей:",
        reply_markup=await InlineMenuRating().menu()
    )
