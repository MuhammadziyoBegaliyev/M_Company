# handlers/start.py
from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.main_kb import main_menu_kb

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Salom! Avtoservis botiga xush kelibsiz.\nQuyidan kerakli bo‘limni tanlang:", 
        reply_markup=main_menu_kb()
    )
