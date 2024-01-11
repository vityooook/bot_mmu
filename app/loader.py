from loguru import logger

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config

logger.add(
    "logs/log_{time}.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="1 day",
    compression="zip"
)

storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=storage)
