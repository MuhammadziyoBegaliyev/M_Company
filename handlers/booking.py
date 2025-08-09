from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from keyboards.inline import kottej_number_kb, add_more_kb  #
from states.booking import Booking
from config import ADMINS

router = Router()

# === 1) Kottej bron qilish ===
@router.callback_query(F.data == "book_kottej")
async def choose_kottej(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(
        photo="https://picsum.photos/600/400",  
        caption="4 kishilik kottejlar. Bizda 8 ta mavjud. Birini tanlang:",
        reply_markup=kottej_number_kb()
    )
    await state.set_state(Booking.waiting_for_kottej_number)

@router.callback_query(F.data.startswith("kottej_"), Booking.waiting_for_kottej_number)
async def kottej_number_selected(callback: CallbackQuery, state: FSMContext):
    number = callback.data.split("_")[1]
    await state.update_data(kottej=number)
    await callback.message.answer(f"Kottej {number} tanlandi. Sana kiriting:")
    await state.set_state(Booking.waiting_for_date)

# === 2) Tapchan, Basseyn, Sauna bron qilish ===
@router.callback_query(F.data.in_({"book_tapchan", "book_basseyn", "book_sauna"}))
async def handle_other_bookings(callback: CallbackQuery, state: FSMContext):
    mapping = {
        "book_tapchan": "Tapchan",
        "book_basseyn": "Basseyn",
        "book_sauna": "Sauna"
    }
    service = mapping.get(callback.data, "Xizmat")
    await state.update_data(extra_service=service)
    await callback.message.answer(f"{service} bron qilindi. Sana kiriting:")
    await state.set_state(Booking.waiting_for_date)

# === 3) Sana kiritish ===
@router.message(Booking.waiting_for_date)
async def get_date(message: Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer("Yana nimadur qo‘shasizmi?", reply_markup=add_more_kb())

# === 4) Tasdiqlash ===
@router.callback_query(F.data == "confirm_booking")
async def confirm(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    summary = (
        "✅ Yangi bron:\n"
        f"🏠 Kottej: {data.get('kottej', '-')}\n"
        f"🛋 Xizmat: {data.get('extra_service', '-')}\n"
        f"📅 Sana: {data.get('date', '-')}\n"
        f"👤 Foydalanuvchi: {callback.from_user.full_name} (@{callback.from_user.username})\n"
        f"🆔 ID: {callback.from_user.id}"
    )

    await callback.message.answer("Broningiz qabul qilindi! Admin bilan bog‘laniladi.")

    for admin_id in ADMINS:
        await callback.bot.send_message(chat_id=admin_id, text=summary)

    await callback.message.answer("Iltimos, fikringizni yuboring:")
    await state.set_state(Booking.waiting_for_feedback)

# === 5) Fikr bildiruvchi qism ===
@router.message(Booking.waiting_for_feedback)
async def feedback(message: Message, state: FSMContext):
    text = message.text
    feedback_msg = (
        f"📝 Fikr:\n{text}\n\n"
        f"👤 Kimdan: {message.from_user.full_name} (@{message.from_user.username})"
    )

    for admin_id in ADMINS:
        await message.bot.send_message(chat_id=admin_id, text=feedback_msg)

    await message.answer("Fikringiz uchun rahmat!")
    await state.clear()
