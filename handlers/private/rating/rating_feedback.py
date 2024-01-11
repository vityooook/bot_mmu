from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from loguru import logger

from keyboard.inline.menu.inline_menu import InlineMenu
from keyboard.inline.rating.inline_feedback import InlineFeedback
from handlers.callback.callback_data import (
    RatingMenuCallback, RatingFeedbackCallback, RatingLinkFeedbackCallback
)
from .question import question
from database import crud

router = Router()


class TeacherFeedback(StatesGroup):
    name = State()
    id = State()


@logger.catch()
@router.callback_query(RatingMenuCallback.filter(F.act == "LEAVE-FEEDBACK"))
async def see_rating(query: CallbackQuery, state: FSMContext):
    # получаем callback из inline_menu_rating
    await query.message.edit_text(
        "<b>Пожалуйста, напиши ФИО преподавателя.</b>"
        "<i>\n\nДля отмены вызови меню, нажав на соответствующую кнопку.</i>"
    )
    await state.set_state(TeacherFeedback.name)


@logger.catch()
@router.message(TeacherFeedback.name)
async def process_selecting_teacher(msg: Message, state: FSMContext):
    # получаем id преподователя, достаем фио из состояния
    teacher_id = await crud.rating.verify_teacher(msg.text.title())
    # если teacher_id = None, то фио не правильное
    if teacher_id:
        # проверяем оставлял ли юзер уже отзыв о это преподователе
        if not await crud.rating.verify_feedback(
                user_id=msg.from_user.id,
                teacher_id=teacher_id
        ):
            name = msg.text.title()
            await state.update_data(name=name, id=teacher_id)
            # вызываем inline кнопки с вопросами
            await msg.answer(
                f"{question[0]}",
                reply_markup=await InlineFeedback().start_feedback()
            )
        else:
            await msg.answer("вы уже оставляли отзыв")
    else:
        await msg.answer("имя фио преподователя не верное")


@logger.catch()
@router.callback_query(RatingLinkFeedbackCallback.filter(F.act == "LINK"))
async def link_to_feedback(
        query: CallbackQuery,
        callback_data: RatingLinkFeedbackCallback,
        state: FSMContext,
):
    # мы ловим callbakc из teacher_rating
    # проверяем оставлял ли юзер отзыв об преподователе
    if not await crud.rating.verify_feedback(
            user_id=query.from_user.id,
            teacher_id=callback_data.teacher_id
    ):
        teacher_name = await crud.rating.get_teacher_name(callback_data.teacher_id)
        await state.update_data(
            name=teacher_name,
            id=callback_data.teacher_id
        )
        # вызываем inline кнопки с вопросами
        await query.message.edit_text(
            f"{question[0]}",
            reply_markup=await InlineFeedback().start_feedback()
        )
    else:
        await query.message.edit_text(
            "вы уже оставляли отзыв"
        )


@logger.catch()
@router.callback_query(RatingFeedbackCallback.filter())
async def process_feedback(
        query: CallbackQuery,
        callback_data: RatingFeedbackCallback,
        state: FSMContext,
        marks: list = []
):
    await query.message.edit_text("мур мур...")
    # достаем ответ из callback
    mark_data = await InlineFeedback().process_selection(
        query=query,
        callback_data=callback_data
    )
    # получаем id препода из состояния
    teacher_data = await state.get_data()
    # делаем проверку на номер ответа
    if mark_data["question"] != 5:
        # добовляем ответ в сипосок
        marks.append(mark_data)
        # вызываем следующий вопрос
        await query.message.edit_text(
            f"{question[mark_data['question']]}",
            reply_markup=await InlineFeedback().start_feedback(
                question=mark_data["question"] + 1
            )
        )
    else:
        # добовляем последний ответ
        marks.append(mark_data)
        # добовляем ответы в дб
        await crud.rating.add_rating(
            teacher_id=teacher_data["id"],
            user_id=query.from_user.id,
            marks=marks
        )
        marks.clear()
        # вызываем основное меню
        await query.message.edit_text(
            "😼 спасибо, ответы записаны 😼"
            "\n\n<b>Выберите нужное действие: </b> ",
            reply_markup=await InlineMenu().menu()
        )
