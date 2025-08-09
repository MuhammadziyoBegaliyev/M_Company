import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import TOKEN

# Jadval yaratish funksiyalarini chaqirish
from database.db import create_tables
from database.promotions import create_promotions_table, create_users_table
from database.contacts import create_contacts_table
from database.menu import create_menu_table
from database.tarifs import create_tarifs_table

# Middleware
from middlewares.i18n import I18nMiddleware

# Routerlar
from handlers.register import router as register_router
from handlers.main_menu import router as main_menu_router
from handlers.booking import router as booking_router
from handlers.admin import router as admin_router
from handlers.feedback import router as feedback_router
from handlers.contact import router as contact_router
from handlers.menu import router as menu_router
from handlers.tarifs import router as tarifs_router
from handlers.user import router as user_router
from handlers.promotions import promotions_router
from handlers.admin_promotions import admin_router as admin_promotions_router

# --- Bot va Dispatcher yaratish ---
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# --- Middleware ulash ---
dp.message.middleware(I18nMiddleware())
dp.callback_query.middleware(I18nMiddleware())

# --- Routerlarni ulash ---
dp.include_router(register_router)
dp.include_router(main_menu_router)
dp.include_router(booking_router)
dp.include_router(admin_router)
dp.include_router(feedback_router)
dp.include_router(contact_router)
dp.include_router(menu_router)
dp.include_router(tarifs_router)
dp.include_router(user_router)
dp.include_router(promotions_router)
dp.include_router(admin_promotions_router)

# --- Asosiy ishga tushirish ---
async def main():
    # Barcha jadval funksiyalarini chaqirish
    await create_tables()
    create_promotions_table()
    create_users_table()
    create_contacts_table()
    create_menu_table()
    create_tarifs_table()

    # Botni ishga tushirish
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
