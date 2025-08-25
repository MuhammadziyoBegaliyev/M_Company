import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage  # FSM uchun storage
from config import BOT_TOKEN
from handlers import start, services, location
from handlers.admin import admin_router
from handlers.booking import booking_router
from database.booking import create_tables

# from utils.geo import haversine_km, find_nearby_providers

# Logging sozlamasi
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
)

async def main():
    # Bot va Dispatcher
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher(storage=MemoryStorage())

    # Bazadagi jadvallarni yaratish
    create_tables() 
    
    # Routerlarni ulash
    dp.include_router(start.router)
    dp.include_router(services.router)
    dp.include_router(location.router)
    dp.include_router(admin_router)
    dp.include_router(booking_router)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Botda xatolik yuz berdi: {e}")

if __name__ == "__main__":
    asyncio.run(main())
