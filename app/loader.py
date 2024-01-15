from loguru import logger

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config

# * Set up logging, declare the bot and dispatcher
logger.add(
    "logs/logs.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="1 day",
    compression="zip"
)

storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=storage)
