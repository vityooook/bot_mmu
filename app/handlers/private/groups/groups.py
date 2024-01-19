from aiogram import Router, F
from aiogram.types import CallbackQuery
from loguru import logger

# * import inline main menu keyboard
from keyboard.inline.menu.inline_menu import main_menu
# * import inline group menu keyboard
from keyboard.inline.groups.inline_groups import back_to_main_menu
# * import some callback
from handlers.callback.callback_data import MenuCallback, GroupsCallback


router = Router()


@logger.catch()
@router.callback_query(MenuCallback.filter(F.act == "GROUPS"))
async def group_menu(query: CallbackQuery):
    """working out a callback for a call group menu

    :param query: this object represents an incoming callback query from a callback button
    :return: the output is several coroutines
    """
    logger.debug("group menu is called")
    await query.message.edit_text(
        "Ссылки на разные группы МЯУ"
        "\n\n<a href='https://t.me/+rFSRBaxmn6NlNjAy'>главная группа МЯУ</a>",
        reply_markup=back_to_main_menu()
    )


@logger.catch()
@router.callback_query(GroupsCallback.filter(F.act == "BACK"))
async def back_menu(query: CallbackQuery):
    """working out a callback for back to main menu

    :param query: this object represents an incoming callback query from a callback button
    :return: the output is several coroutines
    """
    await query.message.edit_text(
        "МЯУ бот создан для студентов.\n\n<b>Выберите нужное действие:</b>",
        reply_markup=main_menu()
    )
