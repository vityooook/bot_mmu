from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from loguru import logger

# * import inline keyboard to return to ratings menu
from keyboard.inline.rating.inline_link_back_rating import leavefeedback_or_back
# * import callback
from handlers.callback.callback_data import RatingMenuCallback
# * import requests to database
from database import crud

router = Router()


class Teacher(StatesGroup):
    name = State()


@logger.catch()
@router.callback_query(RatingMenuCallback.filter(F.act == "SEE-RATING"))
async def see_rating(query: CallbackQuery, state: FSMContext):
    """Working out a callback for see teacher's rating

    :param query: this object represents an incoming callback query from a callback button
    :param state: inherit fsm
    """
    logger.debug("student looking teacher's rating")
    await query.message.edit_text(
        "<b>Пожалуйста, напиши ФИО преподавателя.</b>"
        "<i>\n\nДля отмены вызови меню, нажав на соответствующую кнопку.</i>")
    await state.set_state(Teacher.name)


@logger.catch()
@router.message(Teacher.name)
async def process_selecting_teacher(msg: Message, state: FSMContext):
    """Handling the state when the user entered teacher's name

    :param msg: message sent by the user
    :param state: inherit fsm
    """
    # * check if a teacher exist
    teacher_id = await crud.rating.verify_teacher(msg.text.title())
    # * if Teacher_id = No, this is incorrect
    if teacher_id:
        await state.clear()
        teacher_name = msg.text.title()
        # * get the teacher's qualification using id
        teacher_subject = await crud.rating.get_teacher_subject(teacher_id)
        # * calculation the teacher's rating
        rating = await crud.rating.get_rating(teacher_id)
        # * calculation the teacher's average rating
        rating_avg = await crud.rating.get_avg_rating(teacher_id)
        if rating:
            await msg.answer(
                f"<b>{teacher_name}</b>" 
                f"<i>\nДисциплина: {teacher_subject}</i>"
                f"\n\n<b>Общая оценка:</b> {rating_avg}"
                f"\n\nЗнания: {rating[0][1]}"
                f"\nУмение преподавать: {rating[1][1]}"
                f"\nВ общении: {rating[2][1]}"
                f"\n«Халявность»: {rating[3][1]}"
                f"<i>\n\nМы были бы очень признательны, если вы могли бы поделиться вашим опытом обучения с преподавателем.</i>",
                reply_markup=leavefeedback_or_back(teacher_id=teacher_id)
            )
        else:
            await msg.answer(
                f"<b>{teacher_name}</b>"
                f"<i>\nДисциплина: {teacher_subject}</i>"
                f"\n\n<code>Рейтинг осутствует</code>"
                "<i>\n\nМы были бы очень признательны, если вы могли бы поделиться вашим опытом обучения с преподавателем.</i>",
                reply_markup=leavefeedback_or_back(teacher_id=teacher_id)
            )
    else:
        await msg.answer(
            "Фырк, такого преподавателя не существует! 🙀"
            "\n\n<i>Возможно, ты просто ошибся в имени преподавателя. Напиши заново, пожалуйста</i>"
        )
