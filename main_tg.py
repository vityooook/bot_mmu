import logging
import asyncio
from aiogram import Bot, Dispatcher

from loader import dp, bot
from services import set_default_commands
from celery_queue.tasks import app_celery

import handlers


async def main():
    dp.include_routers(handlers.users.start.router,
                       handlers.schedule.schedule.router)
    await set_default_commands(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    # await asyncio.gather(dp.start_polling(bot), setup_taskiq())
    # await setup_taskiq()
    # logging.info("Queue stating! ")
    await dp.start_polling(bot)
    logging.debug("Bot started!")



async def setup_taskiq():
    await app_celery.worker_main(["-A", "celery_queue.tasks", "worker", "-B"])
    logging.info('tasks work...')


if __name__ == '__main__':
    # asyncio.run(main())
    # setup_taskiq()
    asyncio.get_event_loop().run_until_complete(main())
