from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from dictionary import messages
from keyboards.reply_factory import ReplyKeyboardFactory

router = Router()


@router.message(Command("start"))
async def command_start(message: Message):
    kb = ReplyKeyboardFactory.create(
        texts=[messages["keyboards"]["send_excel"]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await message.answer(messages["greetings"]["start"], reply_markup=kb)
