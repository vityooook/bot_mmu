from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboard.inline.rating.inline_link_back_rating import InlineLinkBackRating
from keyboard.inline.rating.inline_cancel_rating import InlineCancelRating
from handlers.callback.callback_data import RatingMenuCallback, RatingLinkFeedbackCallback
from database import crud
from keyboard.inline.rating.inline_menu_rating import InlineMenuRating

router = Router()


class Teacher(StatesGroup):
    name = State()


@router.callback_query(RatingMenuCallback.filter(F.act == "SEE-RATING"))
async def see_rating(query: CallbackQuery, state: FSMContext):
    await query.message.edit_text("напиши фио преподователя")
    await state.set_state(Teacher.name)


@router.message(Teacher.name)
async def process_selecting_teacher(msg: Message, state: FSMContext):
    teacher_id = crud.rating.verify_teacher(msg.text.title())
    if teacher_id:
        await state.clear()
        teacher_name = msg.text.title()
        teacher_subject = crud.rating.get_teacher_subject(teacher_id)
        rating = crud.rating.get_rating(teacher_id)
        rating_avg = crud.rating.get_avg_rating(teacher_id)
        if rating:
            await msg.answer(
                f"<b>{teacher_name}</b>" 
                f"<i>\nДисциплина: {teacher_subject}</i>"
                f"\n\n<b>Средний балл:</b> {rating_avg}"
                f"\n\nЧувство юмора: {rating[0][1]}"
                f"\nОбъективность: {rating[1][1]}"
                f"\nТребовательность: {rating[2][1]}"
                f"\nИзложение материала: {rating[3][1]}"
                f"\nОрганизованность: {rating[4][1]}"
                f"<i>\n\nМы были бы очень признательны, если вы могли бы поделиться вашим опытом обучения с преподавателем.</i>",
                reply_markup=await InlineLinkBackRating().link_back(
                    teacher_id=teacher_id
                )
            )
        else:
            await msg.answer(
                f"<b>{teacher_name}</b>"
                f"<i>\nДисциплина: {teacher_subject}</i>"
                f"\n\n<code>Рейтинг осутствует</code>"
                "<i>\n\nМы были бы очень признательны, если вы могли бы поделиться вашим опытом обучения с преподавателем.</i>",
                reply_markup=await InlineLinkBackRating().link_back(
                    teacher_id=teacher_id
                )
            )
    else:
        await msg.answer(
            "фио преподователя не верное"
        )


# @router.callback_query(RatingLinkFeedbackCallback.filter(F.act == "BACK"))
# async def teacher_rating(query: CallbackQuery):
#     await query.message.edit_text(
#         text="меню рейтинга преподователей:",
#         reply_markup=await InlineMenuRating().menu()
#     )