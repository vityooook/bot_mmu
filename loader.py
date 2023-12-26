import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config

logging.basicConfig(format=u'%(filename)s:%(lineno)-d #%(levelname)-16s [%(asctime)s] %(message)s',
                    level=logging.INFO)

storage = MemoryStorage()   # TODO: use redis as temporary database
bot = Bot(token=config.B, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=storage)