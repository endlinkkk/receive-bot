from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from dictionary import messages

router = Router()


@router.message(Command("start"))
async def command_start(message: Message):
    await message.answer(messages["greetings"]["start"])
