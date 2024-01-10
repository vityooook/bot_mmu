from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboard.inline.rating.inline_link_back_rating import InlineLinkBackRating
from handlers.callback.callback_data import RatingMenuCallback
from database import crud

router = Router()


class Teacher(StatesGroup):
    name = State()


@router.callback_query(RatingMenuCallback.filter(F.act == "SEE-RATING"))
async def see_rating(query: CallbackQuery, state: FSMContext):
    # получаем callback из inline_menu_rating
    await query.message.edit_text(
        "<b>Пожалуйста, напиши ФИО преподавателя.</b>"
        "<i>\n\nДля отмены вызови меню, нажав на соответствующую кнопку.</i>")
    await state.set_state(Teacher.name)


@router.message(Teacher.name)
async def process_selecting_teacher(msg: Message, state: FSMContext):
    # получаем id преподователя, достаем фио из состояния
    teacher_id = await crud.rating.verify_teacher(msg.text.title())
    # если teacher_id = None, то фио не правильное
    if teacher_id:
        await state.clear()
        teacher_name = msg.text.title()
        teacher_subject = await crud.rating.get_teacher_subject(teacher_id)
        rating = await crud.rating.get_rating(teacher_id)
        rating_avg = await crud.rating.get_avg_rating(teacher_id)
        # если rating = None, то отзывов нету
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
