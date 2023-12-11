from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboard.inline.menu.inline_menu import InlineMenu
from keyboard.inline.groups.inline_groups import InlineGroups
from handlers.callback.callback_data import MenuCallback, GroupsCallback


router = Router()


@router.callback_query(MenuCallback.filter(F.act == "GROUPS"))
async def group_menu(query: CallbackQuery):
    await query.message.edit_text(
        "Ссылки на разные группы МЯУ"
        "\n\n<a href='https://t.me/+rFSRBaxmn6NlNjAy'>главная группа МЯУ</a>",
        reply_markup=await InlineGroups().groups_menu()
    )


@router.callback_query(GroupsCallback.filter(F.act == "BACK"))
async def back_menu(query: CallbackQuery):
    await query.message.edit_text(
        "МЯУ бот создан для студентов.\n\n<b>Выберите нужное действие:</b>",
        reply_markup=await InlineMenu().menu()
    )
