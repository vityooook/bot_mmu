from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from loguru import logger

# * import inline rating menu keyboard
from keyboard.inline.menu.inline_menu import main_menu
from keyboard.inline.rating.inline_feedback import start_feedback
# * import callback
from handlers.callback.callback_data import (
    RatingMenuCallback, RatingFeedbackCallback, RatingLinkFeedbackCallback
)
# * import questions for survey
from .question import question
# * import requests to database
from database import crud

router = Router()


class TeacherFeedback(StatesGroup):
    name = State()
    id = State()


@logger.catch()
@router.callback_query(RatingMenuCallback.filter(F.act == "LEAVE-FEEDBACK"))
async def see_rating(query: CallbackQuery, state: FSMContext):
    """Working out a callback for leave a feedback about teacher

    :param query: this object represents an incoming callback query from a callback button
    :param state: inherit fsm
    """
    logger.debug("student leaves feedback")
    await query.message.edit_text(
        "<b>Пожалуйста, напиши ФИО преподавателя.</b>"
        "<i>\n\nДля отмены вызови меню, нажав на соответствующую кнопку.</i>"
    )
    await state.set_state(TeacherFeedback.name)


@logger.catch()
@router.message(TeacherFeedback.name)
async def process_selecting_teacher(msg: Message, state: FSMContext):
    """Handling the state when the user entered teacher's name

    :param msg: message sent by the user
    :param state: inherit fsm
    """
    # * check if a teacher exist
    teacher_id = await crud.rating.verify_teacher(msg.text.title())
    if teacher_id:
        # * checking whether the student left a review about this teacher
        if not await crud.rating.verify_feedback(
                user_id=msg.from_user.id,
                teacher_id=teacher_id
        ):
            name = msg.text.title()
            await state.update_data(name=name, id=teacher_id)
            # * call inline keyboard with first question
            await msg.answer(
                f"{question[0]}",
                reply_markup=start_feedback()
            )
        else:
            await msg.answer(
                "Фырк,ты уже оставлял отзыв о данном преподавателе."
                "\n\n<i>Для отмены вызови меню, нажав на соответствующую кнопку.</i>"
            )
    else:
        await msg.answer(
            "Фырк, такого преподавателя не существует! 🙀"
            "\n\n<i>Возможно, ты просто ошибся в имени преподавателя. Напиши заново, пожалуйста</i>"
        )


@logger.catch()
@router.callback_query(RatingLinkFeedbackCallback.filter(F.act == "LINK"))
async def link_to_feedback(
        query: CallbackQuery,
        callback_data: RatingLinkFeedbackCallback,
        state: FSMContext,
):
    """Catch callback from teacher_python.py

    :param query: this object represents an incoming callback query from a callback button
    :param callback_data: the callback with some information
    :param state: inherit fsm
    """
    # * checking whether the student left a review about this teacher
    if not await crud.rating.verify_feedback(
            user_id=query.from_user.id,
            teacher_id=callback_data.teacher_id
    ):
        # * get the teacher's name
        teacher_name = await crud.rating.get_teacher_name(callback_data.teacher_id)
        await state.update_data(
            name=teacher_name,
            id=callback_data.teacher_id
        )
        # * call inline keyboard with first question
        await query.message.edit_text(
            f"{question[0]}",
            reply_markup=start_feedback()
        )
    else:
        await query.message.edit_text(
            "Фырк,ты уже оставлял отзыв о данном преподавателе."
            "\n\n<i>Для отмены вызови меню, нажав на соответствующую кнопку.</i>"
        )


@logger.catch()
@router.callback_query(RatingFeedbackCallback.filter())
async def process_feedback(
        query: CallbackQuery,
        callback_data: RatingFeedbackCallback,
        state: FSMContext,
        marks: list = []
):
    """Working out a callback for catch marks

        :param query: this object represents an incoming callback query from a callback button
        :param callback_data: the callback with some information
        :param state: inherit fsm
        """
    await query.message.edit_text("мур мур...")
    # * get the response from callback
    mark_data = {"mark": callback_data.act, "question": callback_data.question}
    # * get the teacher id from state
    teacher_data = await state.get_data()
    # * check the question number
    if mark_data["question"] != 5:
        # * add answer to list
        marks.append(mark_data)
        # * call the next question
        await query.message.edit_text(
            f"{question[mark_data['question']]}",
            reply_markup=start_feedback(
                question=mark_data["question"] + 1
            )
        )
    else:
        # * add last answer to list
        marks.append(mark_data)
        # * add all answer to the database
        await crud.rating.add_rating(
            teacher_id=teacher_data["id"],
            user_id=query.from_user.id,
            marks=marks
        )
        marks.clear()
        # * call main menu
        await query.message.edit_text(
            "😼 спасибо, ответы записаны 😼"
            "\n\n<b>Выберите нужное действие: </b> ",
            reply_markup=main_menu()
        )
