from aiogram import Router, types, F
from aiogram.filters import Command
from database.booking import add_service, delete_service, get_all_services

admin_router = Router()

ADMIN_ID = 123456789  # 📌 Bu yerga admin Telegram ID qo‘yiladi

# 📌 Admin panel menyusi
@admin_router.message(Command("admin"))
async def admin_panel(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("🔐 Admin panel:\n\n1. /add_service\n2. /delete_service\n3. /all_services")
    else:
        await message.answer("❌ Siz admin emassiz!")

# 📌 Yangi servis qo‘shish
@admin_router.message(Command("add_service"))
async def add_new_service(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Siz admin emassiz!")

    try:
        parts = message.text.split(maxsplit=3)
        name = parts[1]
        description = parts[2]
        photo = parts[3]
        add_service(name, description, photo)
        await message.answer(f"✅ Servis qo‘shildi:\n📌 {name}")
    except:
        await message.answer("❌ Format noto‘g‘ri!\nNamuna: `/add_service Sauna 'Issiq sauna' sauna.jpg`")

# 📌 Servis o‘chirish
@admin_router.message(Command("delete_service"))
async def delete_service_cmd(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Siz admin emassiz!")

    try:
        service_id = int(message.text.split()[1])
        delete_service(service_id)
        await message.answer(f"🗑 Servis ID {service_id} o‘chirildi!")
    except:
        await message.answer("❌ Format noto‘g‘ri!\nNamuna: `/delete_service 1`")

# 📌 Barcha servislarni ko‘rish
@admin_router.message(Command("all_services"))
async def all_services_cmd(message: types.Message):
    services = get_all_services()
    if not services:
        await message.answer("⚠️ Servislar mavjud emas")
    else:
        text = "📋 Servislar ro‘yxati:\n\n"
        for s in services:
            text += f"ID: {s[0]} | {s[1]} \n📄 {s[2]}\n🖼 {s[3]}\n\n"
        await message.answer(text)
