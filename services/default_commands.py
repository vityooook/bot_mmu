from aiogram import Dispatcher, Bot



async def set_default_commands(bot: Bot):
    await bot.set_my_commands()
