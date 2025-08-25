from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from datetime import datetime

from keyboards.services_kb import services_filter_kb
from keyboards.main_kb import main_menu_kb
from states.service_state import ServiceStates
from config import ADMIN_ID

router = Router()


# --- ReplyKeyboard orqali xizmatlar menyusi ---
@router.message(F.text == "Автосервисы")
async def services_menu(message: Message, state: FSMContext):
    await state.set_state(ServiceStates.waiting_service_filter)
    await message.answer(
        "🔍 Выберите нужный вид услуги:",
        reply_markup=services_filter_kb()
    )


# --- Inline tugmalar orqali xizmat tanlash ---
@router.callback_query(F.data.startswith("service:"))
async def process_service_choice(callback: CallbackQuery, state: FSMContext):
    """
    callback_data formati: service:{tag}:{title}
    Masalan: service:oil_change:Замена масла
    """
    parts = callback.data.split(":", 2)
    if len(parts) == 3:
        _, tag, service_text = parts
    else:
        service_text = "❓ Неизвестная услуга"

    # Foydalanuvchiga javob
    await callback.message.answer(
        f"✅ Вы выбрали услугу: <b>{service_text}</b>.\n\n"
        f"Наши специалисты скоро свяжутся с вами 📞",
        parse_mode="HTML"
    )

    # 🕒 Joriy vaqt
    now = datetime.now().strftime("%d.%m.%Y %H:%M")

    # 🛠 Adminga yuboriladigan xabar
    user = callback.from_user
    admin_message = (
        f"📩 <b>Новая заявка!</b>\n\n"
        f"👤 Имя: {user.full_name}\n"
        f"🆔 ID: <code>{user.id}</code>\n"
        f"🔗 Username: @{user.username if user.username else 'нет'}\n"
        f"🚗 Услуга: <b>{service_text}</b>\n"
        f"🕒 Время: <i>{now}</i>"
    )
    await callback.bot.send_message(ADMIN_ID, admin_message, parse_mode="HTML")

    await state.clear()
    await callback.answer("✅ Услуга выбрана")


# --- Orqaga tugmasi ---
@router.callback_query(F.data == "back:menu")
async def back_to_menu_callback(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("🏠 Главное меню", reply_markup=main_menu_kb())
    await callback.answer()
