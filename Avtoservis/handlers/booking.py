from aiogram import Router, types, F
from database.booking import get_all_services

booking_router = Router()

# 📌 Servislarni ko‘rsatish
@booking_router.message(F.text == "🏠 Servislar")
async def show_services(message: types.Message):
    services = get_all_services()
    if not services:
        await message.answer("⚠️ Hozircha servislar mavjud emas")
    else:
        for s in services:
            await message.answer_photo(
                photo=s[3],
                caption=f"🏷 {s[1]}\n📄 {s[2]}"
            )


from aiogram import Router, types, F

booking_router = Router()

@booking_router.message(F.text == "Бензин доставка")
async def booking_start(message: types.Message):
    await message.answer("⛽️ Bensin yetkazib berish xizmati ishga tushdi!")
