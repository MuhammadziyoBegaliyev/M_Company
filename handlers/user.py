from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from states.register import RegisterState
from aiogram.fsm.context import FSMContext
from database.db import add_user
from keyboards.user_kb import main_menu_kb

router = Router()

@router.message(F.text == "/start")
async def start_cmd(message: Message, state: FSMContext, locale):
    await message.answer(locale["welcome"])
    await message.answer(locale["enter_name"])
    await state.set_state(RegisterState.name)

@router.message(RegisterState.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="📞 Telefon raqamini yuborish", request_contact=True)]], resize_keyboard=True)
    await message.answer("Telefon raqamingizni yuboring:", reply_markup=kb)
    await state.set_state(RegisterState.phone)

@router.message(RegisterState.phone)
async def register_phone(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text
    await state.update_data(phone=phone)
    kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇷🇺 Русский")]], resize_keyboard=True)
    await message.answer("Tilni tanlang:", reply_markup=kb)
    await state.set_state(RegisterState.language)

@router.message(RegisterState.language)
async def register_language(message: Message, state: FSMContext):
    lang = "uz" if "O'zbekcha" in message.text else "ru"
    data = await state.get_data()
    await add_user(message.from_user.id, data["name"], data["phone"], lang)
    await message.answer("✅ Ro'yxatdan o'tdingiz!", reply_markup=main_menu_kb(lang))
    await state.clear()
