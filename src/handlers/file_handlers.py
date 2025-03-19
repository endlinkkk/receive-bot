from pathlib import Path

from aiogram import Bot, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from config import settings
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
        text=messages["instructions"]["canceling_file_sending"],
        reply_markup=ReplyKeyboardRemove(),
    )


async def _download_file(bot: Bot, file_id: str, file_name: str) -> Path:
    try:
        file = await bot.get_file(file_id)

        upload_dir = Path(settings.UPLOAD_DIR).absolute()
        upload_dir.mkdir(parents=True, exist_ok=True)

        # Полный путь к файлу
        file_path = upload_dir / file_name

        await bot.download_file(file.file_path, destination=file_path)
        return file_path
    except Exception:
        raise ValueError(messages["errors"]["download_failed"])


@router.message(F.document)
async def handle_excel_file(message: Message, state: FSMContext):
    try:
        if not message.document.file_name.endswith((".xlsx", ".xls")):
            raise ValueError(messages["errors"]["invalid_format"])

        file_path = await _download_file(
            message.bot, message.document.file_id, Path(message.document.file_name).name
        )
        response = str(file_path.absolute())

    except ValueError as e:
        response = str(e)
    except Exception:
        response = messages["errors"]["general"]

    await message.answer(text=response, reply_markup=ReplyKeyboardRemove())
    await state.clear()


@router.message(SendFile.waiting_for_file)
async def waiting_file(message: Message, state: FSMContext):
    await message.answer(text=messages["instructions"]["waiting_for_file"])
