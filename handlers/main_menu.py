from aiogram import Router, F
from aiogram.types import (
    Message, CallbackQuery,
    ReplyKeyboardMarkup, KeyboardButton
)
from keyboards.inline import language_inline_kb, contact_kb, booking_menu_kb
from keyboards.location_kb import location_kb
from keyboards.reply import main_menu_kb
from database.db import update_user_language

router = Router()

# 📌 1) Asosiy menyu tugmalari
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏠 Bron qilish")],  # BRON QILISH tugmasi
        [KeyboardButton(text="🍽 Menyu")],
        [KeyboardButton(text="🏷️ Maxsus tariflar")],
        [KeyboardButton(text="📍 Lokatsiya"), KeyboardButton(text="☎️ Murojaat")],
        [KeyboardButton(text="🌐 Tilni o‘zgartirish")]
    ],
    resize_keyboard=True
)

# 📌 2) Asosiy menyuni qaytaruvchi funksiya (til bilan)
def main_menu_kb(lang="uz"):
    return main_menu

# 📌 3) Tilni o‘zgartirish menyusi
@router.message(F.text.contains("🌐 Tilni o‘zgartirish"))
async def change_lang_menu(message: Message, locale):
    await message.answer(locale["choose_language"], reply_markup=language_inline_kb())

# 📌 4) Inline tugmadan tilni o‘zgartirish
@router.callback_query(F.data.startswith("lang_"))
async def process_change_lang(callback: CallbackQuery, locale):
    new_lang = callback.data.split("_")[1]
    await update_user_language(callback.from_user.id, new_lang)
    await callback.message.edit_text(locale["language_changed"])
    await callback.message.answer(locale["main_menu"], reply_markup=main_menu_kb(new_lang))

# 📌 5) Orqaga - asosiy menyuga qaytish
@router.callback_query(F.data == "back_main")
async def back_to_main(callback: CallbackQuery, locale):
    await callback.message.edit_text(locale["main_menu"], reply_markup=main_menu_kb())

# 📌 6) Lokatsiya
@router.message(F.text == "📍 Lokatsiya")
async def send_location(message: Message, locale):
    await message.answer(
        f"📍 <b>Bizning manzil:</b>\n\n"
        f"Toshkent shahar, Chilonzor tumani, Kottej hududi.\n\n"
        f"<i>Quyidagi tugmani bosing:</i>",
        reply_markup=location_kb()
    )
    await message.answer_location(
        latitude=41.311081,
        longitude=69.240562
    )

# 📌 7) Murojaat
@router.message(F.text == "☎️ Murojaat")
async def contact_info(message: Message, locale):
    await message.answer(
        "☎️ <b>Murojaat uchun kontaktlar:</b>\n\n"
        "📞 Telefon: +998 90 143 10 51\n"
        "💬 Operator bilan bog‘lanish uchun tugmani bosing:",
        reply_markup=contact_kb()
    )

# 📌 8) Menyu (agar kerak bo‘lsa)
@router.message(F.text == "🍽 Menyu")
async def show_menu(message: Message, locale):
    await message.answer(
        "🍽 <b>Bizning menyu:</b>\n\n"
        "Menyu tafsilotlari hozircha tayyorlanmoqda..."
    )

# 📌 9) Maxsus tariflar
@router.message(F.text == "🏷️ Maxsus tariflar")
async def show_tarifs(message: Message, locale):
    await message.answer(
        "🏷️ <b>Bizning maxsus tariflar:</b>\n\n"
        "Tariflar ro‘yxati va tafsilotlar tez orada..."
    )

# 📌 10) Bron qilish - booking menu inline tugmalar bilan
@router.message(F.text == "🏠 Bron qilish")
async def booking_menu(message: Message, locale):
    await message.answer(
        "🏠 <b>Bron qilish bo‘limi:</b>\n\n"
        "Qaysi xizmatni bron qilmoqchisiz?",
        reply_markup=booking_menu_kb()
    )
