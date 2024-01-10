from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from handlers.callback.callback_data import MenuCallback, SitingCallback
from keyboard.inline.menu.inline_menu import InlineMenu
from keyboard.inline.siting.inline_siting import InlineSiting
from database import crud

router = Router()


class UserChangeInfo(StatesGroup):
    user_group = State()


@router.callback_query(MenuCallback.filter(F.act == "SITING"))
async def siting_menu(query: CallbackQuery):
    await query.message.edit_text(
        "настроки",
        reply_markup=await InlineSiting().siting_menu()
    )


@router.callback_query(SitingCallback.filter(F.act == "CHANGE-GROUP"))
async def changing_group(query: CallbackQuery, state: FSMContext):
    await state.set_state(UserChangeInfo.user_group)
    await query.message.edit_text("Напищи название твоей группы (пример: ЭКН11-1)")


@router.message(UserChangeInfo.user_group)
async def process_user_group(msg: Message, state: FSMContext):
    group_id = await crud.group.verify_group(msg.text.upper())
    if group_id:
        await state.clear()
        await crud.group.update_group(user_id=msg.from_user.id, group_id=group_id)
        await msg.answer(
            "😼 группу поменяли 😼"
            "\n\n<b>Выберите нужное действие: </b> ",
            reply_markup=await InlineMenu().menu()
        )
    else:
        await msg.answer('такой группы нету')


@router.callback_query(SitingCallback.filter(F.act == "BACK"))
async def back_manu(query: CallbackQuery):
    await query.message.edit_text(
        "\n\n<b>Выберите нужное действие: </b> ",
        reply_markup=await InlineMenu().menu()
    )