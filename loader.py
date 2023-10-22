import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from data import config

logging.basicConfig(format=u'%(filename)s:%(lineno)-d #%(levelname)-16s [%(asctime)s] %(message)s',
                    level=logging.INFO)

storage = MemoryStorage()   # TODO: use redis as temporary database
bot = Bot(token=config.TOKEN)
dp = Dispatcher(storage=storage)