import logging
import asyncio

from loader import dp, bot
from services import set_default_commands

import handlers


async def main():
    logging.debug("Start bot...")
    await set_default_commands(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())
