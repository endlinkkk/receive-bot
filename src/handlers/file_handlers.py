from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from dictionary import messages
from keyboards.reply_factory import ReplyKeyboardFactory

router = Router()


class SendFile(StatesGroup):
    waiting_for_file = State()


@router.message(F.text == messages["keyboards"]["send_excel"])
async def preparing_to_send_a_file(message: Message, state: FSMContext):
    kb = ReplyKeyboardFactory.create(
        texts=[messages["keyboards"]["cancel"]],
        resize_keyboard=True,
    )
    await state.set_state(SendFile.waiting_for_file)
    await message.answer(text=messages["instructions"]["send_excel"], reply_markup=kb)


@router.message(F.text == messages["keyboards"]["cancel"])
async def cancellation_of_sending(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text=messages["instructions"]["canceling_file_sending"], reply_markup=ReplyKeyboardRemove()
    )


@router.message(SendFile.waiting_for_file)
async def waiting_file(message: Message, state: FSMContext):
    await message.answer(text=messages["instructions"]["waiting_for_file"])
