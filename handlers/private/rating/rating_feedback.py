from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboard.inline.menu.inline_menu import InlineMenu
from keyboard.inline.rating.inline_menu_rating import InlineMenuRating
from keyboard.inline.rating.inline_cancel_rating import InlineCancelRating
from keyboard.inline.rating.inline_feedback import InlineFeedback
from handlers.callback.callback_data import RatingMenuCallback, RatingCancelCallback, \
    RatingFeedbackCallback, RatingLinkFeedbackCallback
from database.crud.rating import add_rating
from .question import question
from database import crud

router = Router()


class TeacherFeedback(StatesGroup):
    name = State()
    id = State()


@router.callback_query(RatingMenuCallback.filter(F.act == "LEAVE-FEEDBACK"))
async def see_rating(query: CallbackQuery, state: FSMContext):
    await query.message.edit_text(
        "<b>Пожалуйста, напиши ФИО преподавателя.</b>"
        "<i>\n\nДля отмены вызови меню, нажав на соответствующую кнопку.</i>"
    )
    await state.set_state(TeacherFeedback.name)


@router.message(TeacherFeedback.name)
async def process_selecting_teacher(msg: Message, state: FSMContext):
    teacher_id = crud.rating.verify_teacher(msg.text.title())
    if teacher_id:
        if not crud.rating.verify_feedback(
                user_id=msg.from_user.id,
                teacher_id=teacher_id
        ):
            name = msg.text.title()
            await state.update_data(name=name, id=teacher_id)
            await msg.answer(
                f"{question[0]}",
                reply_markup=await InlineFeedback().start_feedback()
            )
        else:
            await msg.answer("вы уже оставляли отзыв")
    else:
        await msg.answer("имя фио преподователя не верное")


@router.callback_query(RatingLinkFeedbackCallback.filter(F.act == "LINK"))
async def link_to_feedback(
        query: CallbackQuery,
        callback_data: RatingLinkFeedbackCallback,
        state: FSMContext,
):
    if not crud.rating.verify_feedback(
            user_id=query.from_user.id,
            teacher_id=callback_data.teacher_id
    ):
        teacher_name = crud.rating.get_teacher_name(callback_data.teacher_id)
        await state.update_data(
            name=teacher_name,
            id=callback_data.teacher_id
        )
        await query.message.edit_text(
            f"{question[0]}",
            reply_markup=await InlineFeedback().start_feedback()
        )
    else:
        await query.message.edit_text(
            "вы уже оставляли отзыв"
        )


@router.callback_query(RatingFeedbackCallback.filter())
async def process_feedback(
        query: CallbackQuery,
        callback_data: RatingFeedbackCallback,
        state: FSMContext,
        marks: list = []
):
    await query.message.edit_text("мур мур...")
    mark_data = await InlineFeedback().process_selection(
        query=query,
        callback_data=callback_data
    )
    teacher_data = await state.get_data()
    if mark_data["select"] and mark_data["question"] != 5:
        del mark_data["select"]
        marks.append(mark_data)
        await query.message.edit_text(
            f"{question[mark_data['question']]}",
            reply_markup=await InlineFeedback().start_feedback(
                question=mark_data["question"] + 1
            )
        )
    else:
        del mark_data["select"]
        marks.append(mark_data)
        add_rating(
            teacher_id=teacher_data["id"],
            user_id=query.from_user.id,
            marks=marks
        )
        marks.clear()
        await query.message.edit_text(
            "😼 спасибо, ответы записаны 😼"
            "\n\n<b>Выберите нужное действие: </b> ",
            reply_markup=await InlineMenu().menu()
        )
