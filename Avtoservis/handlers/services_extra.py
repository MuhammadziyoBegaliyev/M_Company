# handlers/services_extra.py
from aiogram import Router, F
from aiogram.types import Message
from config import ADMIN_ID

router = Router()

# --- Эвакуатор ---
@router.message(F.text == "Эвакуатор")
async def tow_truck(message: Message):
    await message.answer(
        "🚛 Вам нужен эвакуатор.\nНаш оператор скоро свяжется с вами!"
    )
    # Adminga yuboramiz
    await message.bot.send_message(
        ADMIN_ID,
        f"📢 Новый заказ!\n\n👤 Пользователь: {message.from_user.full_name}\n🆔 ID: {message.from_user.id}\n"
        f"Услуга: 🚛 Эвакуатор"
    )

# --- Бензин доставка ---
@router.message(F.text == "Бензин доставка")
async def fuel_delivery(message: Message):
    await message.answer(
        "⛽ Вы выбрали услугу: доставка бензина.\nНаш оператор скоро свяжется с вами!"
    )
    await message.bot.send_message(
        ADMIN_ID,
        f"📢 Новый заказ!\n\n👤 Пользователь: {message.from_user.full_name}\n🆔 ID: {message.from_user.id}\n"
        f"Услуга: ⛽ Доставка бензина"
    )

# --- Антиблокировка ---
@router.message(F.text == "Антиблокировка")
async def antiblock(message: Message):
    await message.answer(
        "🔑 Услуга антиблокировки.\nНаш специалист свяжется с вами!"
    )
    await message.bot.send_message(
        ADMIN_ID,
        f"📢 Новый заказ!\n\n👤 Пользователь: {message.from_user.full_name}\n🆔 ID: {message.from_user.id}\n"
        f"Услуга: 🔑 Антиблокировка"
    )
