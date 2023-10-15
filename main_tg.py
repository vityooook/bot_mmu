import logging
import asyncio

from loader import dp, bot
from services import set_default_commands
from celery_queue.tasks import app_celery


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await set_default_commands(dp)
    logging.debug("Bot started!")
    print('start')
    await dp.start_polling(bot)
    # dp.startup.register(on_startup)


# def setup_taskiq():
#     app_celery.worker_main(["-A", "celery_queue.tasks", "worker", "-B"])
#     logging.info('tasks work...')


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())
    # setup_taskiq()
