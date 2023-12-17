from loguru import logger
import asyncio

from loader import dp, bot
from services import set_default_commands
from celery_queue.tasks import app_celery
from database.models import register_models_database

from handlers import get_handlers_router


@logger.catch()
async def main():
    
    dp.include_router(get_handlers_router())
    await set_default_commands(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    register_models_database()
    
    # await asyncio.gather(dp.start_polling(bot), setup_taskiq())
    # await setup_taskiq()
    # logging.info("Queue stating! ")
    logger.debug("Bot started!")
    await dp.start_polling(bot)


@logger.catch()
async def setup_taskiq():
    await app_celery.worker_main(["-A", "celery_queue.tasks", "worker", "-B"])
    logger.debug("tasks work...")


if __name__ == "__main__":
    # asyncio.run(main())
    # setup_taskiq()
    asyncio.get_event_loop().run_until_complete(main())
