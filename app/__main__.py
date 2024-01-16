from loguru import logger
import asyncio

from loader import dp, bot
# * import default commands for menu /start
from services import set_default_commands
# * import all routers
from handlers import get_handlers_router


async def main():
    # * declare all routers(handlers) in dispatcher
    dp.include_router(get_handlers_router())
    await set_default_commands(dp)
    # * delete old line command
    await bot.delete_webhook(drop_pending_updates=True)
    logger.debug("Bot started!")
    # * launch bot
    await dp.start_polling(bot)




# @logger.catch()
# async def setup_taskiq():
#     await app_celery.worker_main(["-A", "celery_queue.tasks", "worker", "-B"])


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
