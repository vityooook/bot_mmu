import sys
from loguru import logger

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config

logger.add("log_{time}.log", rotation="1 week", compression="zip")
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")

storage = MemoryStorage()  # TODO: use redis as temporary database
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=storage)
