from aiogram import types, Dispatcher
from loader import bot


async def set_default_commands(dp: Dispatcher):
    await bot.set_my_commands(
        [
            types.BotCommand(command='start', description='Запустить бота'),
        ],
        scope=types.BotCommandScopeAllPrivateChats(),
    )
