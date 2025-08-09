# handlers/admin_promotions.py

from aiogram import Router, F
from aiogram.types import Message
from database.promotions import add_promotion, get_promotions, delete_promotion, get_all_users
from aiogram import Bot

# Router
admin_router = Router()

# ADMIN ID lar ro‘yxati
ADMIN_IDS = [6824528065]  # O‘zgartir: o‘zingni Telegram ID qo‘y

# ➕ Aksiya qo‘shish
@admin_router.message(F.text.startswith("/addpromo"))
async def add_promo(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("❌ Siz admin emassiz.")
        return

    parts = message.text.split("|")
    if len(parts) < 3:
        await message.answer("ℹ️ Format: /addpromo | Sarlavha | Tavsif")
        return

    _, title, desc = parts
    add_promotion(title.strip(), desc.strip())
    await message.answer(f"✅ Aksiya qo‘shildi:\n\n<b>{title.strip()}</b>")

# 📋 Aksiya ro‘yxati
@admin_router.message(F.text.startswith("/promolist"))
async def promo_list(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("❌ Siz admin emassiz.")
        return

    promos = get_promotions()
    if not promos:
        await message.answer("ℹ️ Hech qanday aksiya topilmadi.")
        return

    text = "📋 <b>Aksiyalar ro‘yxati:</b>\n\n"
    for promo in promos:
        promo_id, title, desc = promo
        text += f"ID: <b>{promo_id}</b>\nSarlavha: {title}\nTavsif: {desc}\n\n"

    await message.answer(text)

# ❌ Aksiya o‘chirish
@admin_router.message(F.text.startswith("/delpromo"))
async def promo_delete(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("❌ Siz admin emassiz.")
        return

    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("ℹ️ Format: /delpromo ID")
        return

    promo_id = int(parts[1])
    delete_promotion(promo_id)
    await message.answer(f"✅ Aksiya ID <b>{promo_id}</b> o‘chirildi.")

# 📢 Aksiyani hamma foydalanuvchiga yuborish
@admin_router.message(F.text.startswith("/sendpromo"))
async def promo_broadcast(message: Message, bot: Bot):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("❌ Siz admin emassiz.")
        return

    promos = get_promotions()
    if not promos:
        await message.answer("ℹ️ Hech qanday aksiya topilmadi.")
        return

    text = "📢 <b>Bizning maxsus aksiya:</b>\n\n"
    for promo in promos:
        _, title, desc = promo
        text += f"<b>{title}</b>\n{desc}\n\n"

    users = get_all_users()
    success = 0
    for user in users:
        try:
            await bot.send_message(chat_id=user[0], text=text)
            success += 1
        except Exception as e:
            print(f"❌ Xatolik: {e}")

    await message.answer(f"✅ Aksiya {success} ta foydalanuvchiga yuborildi.")
