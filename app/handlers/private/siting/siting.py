from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from loguru import logger

# * import callback
from handlers.callback.callback_data import MenuCallback, SitingCallback
# * import inline rating menu keyboard
from keyboard.inline.menu.inline_menu import main_menu
# * import inline siting menu keyboard
from keyboard.inline.siting.inline_siting import siting_menu
# * import requests to database
from database import crud

router = Router()


class UserChangeInfo(StatesGroup):
    user_group = State()


@logger.catch()
@router.callback_query(MenuCallback.filter(F.act == "SITING"))
async def siting(query: CallbackQuery):
    """Working out a callback for a call siting menu

    :param query: this object represents an incoming callback query from a callback button
    """
    logger.info("Siting menu is called")
    await query.message.edit_text(
        "🪦 <b>настроки</b> 🪦\n\n"
        "<i>Если у вас возникли какие-либо проблемы, вопросы или у вас есть предложения, не стесняйтесь писать сюда:</i> @manager_miu",
        reply_markup=siting_menu()
    )


@logger.catch()
@router.callback_query(SitingCallback.filter(F.act == "CHANGE-GROUP"))
async def changing_group(query: CallbackQuery, state: FSMContext):
    """Working out a callback for update student's group

    :param query: this object represents an incoming callback query from a callback button
    :param state: inherit fsm
    """
    await state.set_state(UserChangeInfo.user_group)
    await query.message.edit_text("Напищи мне название своей группы (например: ЛПП141-1)")


@logger.catch()
@router.message(UserChangeInfo.user_group)
async def process_user_group(msg: Message, state: FSMContext):
    """Handling the state when the student entered group name

    :param msg: message sent by the user
    :param state: inherit fsm
    """
    # * check if the group exists
    group_id = await crud.group.verify_group(msg.text.upper())
    if group_id:
        await state.clear()
        await crud.group.update_group(user_id=msg.from_user.id, group_id=group_id)
        await msg.answer(
            "😼 группу поменяли 😼"
            "\n\n<b>Выберите нужное действие: </b> ",
            reply_markup=main_menu()
        )
    else:
        await msg.answer(
            "Фырк, такой группы не найдено🙀"
            "\n\n<i>Возможно, ты просто ошибся в названии группы. Напиши заново, пожалуйста.</i>"
        )


@logger.catch()
@router.callback_query(SitingCallback.filter(F.act == "BACK"))
async def back_manu(query: CallbackQuery):
    """Working out a callback for back to main menu

    :param query: this object represents an incoming callback query from a callback button
    """
    await query.message.edit_text(
        "Мяу-мяу-мяу😻"
        "\n\n<b>Выберите нужное действие: </b>",
        reply_markup=main_menu()
    )