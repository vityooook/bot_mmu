from aiogram import types, Dispatcher
from loader import bot



async def set_default_commands(dp: Dispatcher):
    await bot.set_my_commands(
        [
            types.BotCommand(command='start', description='Запустить бота'),
            types.BotCommand(command='schedule', description='расписание'),
            types.BotCommand(command='test', description='тест')
        ],
        scope=types.BotCommandScopeAllPrivateChats(),
    )
