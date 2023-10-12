import logging
import asyncio

from loader import dp, bot
from services import set_default_commands
from celery_queue.tasks import app_celery
import handlers


# def on_startup():
#     logging.info("Start bot...")


async def main():
    await set_default_commands(dp)
    app_celery.worker_main(["-A", "celery_queue.tasks", "worker", "-B"])
    logging.info("Bot started!")
    await dp.start_polling(bot)
    # dp.startup.register(on_startup)


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())
