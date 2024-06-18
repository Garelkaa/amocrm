import asyncio
import logging
import sys

from handlers.user import user
from siganature import bot, dp


async def main():
    dp.include_router(user)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')