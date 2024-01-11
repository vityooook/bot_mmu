from loguru import logger
import asyncio

from loader import dp, bot
from services import set_default_commands
# from database import proceed_schemas

from handlers import get_handlers_router


@logger.catch()
async def main():
    async with bot.session:
        dp.include_router(get_handlers_router())
        await set_default_commands(dp)
        await bot.delete_webhook(drop_pending_updates=True)
    # await proceed_schemas()
        logger.debug("Bot started!")
        await dp.start_polling(bot)




# @logger.catch()
# async def setup_taskiq():
#     await app_celery.worker_main(["-A", "celery_queue.tasks", "worker", "-B"])


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
