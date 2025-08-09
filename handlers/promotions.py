# handlers/promotions.py

from aiogram import Router , F
from aiogram.types import Message
from database.promotions import get_promotions

promotions_router = Router()


@promotions_router.message(F.text == "🎉 Aksiyalar")
async def show_promotions(message: Message):
    promotions = get_promotions()
    if not promotions:
        return await message.answer("Hozircha aksiyalar yo‘q.")
    text = "📣 <b>Aktual Aksiyalar:</b>\n\n"
    for promo in promotions:
        text += f"🔹 <b>{promo[0]}</b>\n{promo[1]}\n\n"
    await message.answer(text, parse_mode="HTML")
