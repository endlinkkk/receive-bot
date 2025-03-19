import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from config import settings
from handlers import commands, file_handlers

bot_commands = [
    BotCommand(command="start", description="start command"),
]


async def setup_bot():
    bot = Bot(token=settings.BOT_TOKEN)
    await bot.set_my_commands(bot_commands)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(file_handlers.router)

    await dp.start_polling(bot)


async def main():
    await setup_bot()


if __name__ == "__main__":
    asyncio.run(main())
