from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.promotions import add_promotion, get_promotions, delete_promotion

router = Router()

# --- STATES ---
class PromotionStates(StatesGroup):
    waiting_for_title = State()
    waiting_for_description = State()

# --- ADMIN MENU ---
@router.message(Command("admin"))
async def admin_menu(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ Aksiya qo‘shish", callback_data="add_promo")],
        [InlineKeyboardButton(text="🗑 Aksiyalarni o‘chirish", callback_data="delete_promo")],
        [InlineKeyboardButton(text="📋 Aksiyalar ro‘yxati", callback_data="list_promos")],
    ])
    await message.answer("🔧 Admin panel:", reply_markup=keyboard)

# --- ADD PROMOTION ---
@router.callback_query(F.data == "add_promo")
async def ask_promo_title(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("📝 Aksiya sarlavhasini kiriting:")
    await state.set_state(PromotionStates.waiting_for_title)
    await callback.answer()

@router.message(PromotionStates.waiting_for_title)
async def get_promo_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("✏️ Aksiya tavsifini kiriting:")
    await state.set_state(PromotionStates.waiting_for_description)

@router.message(PromotionStates.waiting_for_description)
async def get_promo_description(message: Message, state: FSMContext):
    data = await state.get_data()
    title = data.get("title")
    description = message.text

    add_promotion(title, description)
    await message.answer("✅ Aksiya muvaffaqiyatli qo‘shildi.")
    await state.clear()

# --- LIST PROMOTIONS ---
@router.callback_query(F.data == "list_promos")
async def list_promotions(callback: CallbackQuery):
    promotions = get_promotions()
    if not promotions:
        await callback.message.answer("❌ Aksiya mavjud emas.")
    else:
        msg = "📋 Aksiyalar ro‘yxati:\n\n"
        for promo in promotions:
            msg += f"🆔 {promo[0]}\n📌 {promo[1]}\n📝 {promo[2]}\n\n"
        await callback.message.answer(msg)
    await callback.answer()

# --- DELETE PROMOTIONS LIST ---
@router.callback_query(F.data == "delete_promo")
async def choose_promotion_to_delete(callback: CallbackQuery):
    promotions = get_promotions()
    if not promotions:
        await callback.message.answer("🗑 O‘chirish uchun aksiya topilmadi.")
        return

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"❌ {p[1]}", callback_data=f"remove_{p[0]}")] for p in promotions
    ])
    await callback.message.answer("🗑 O‘chirmoqchi bo‘lgan aksiyani tanlang:", reply_markup=keyboard)
    await callback.answer()

# --- DELETE CONFIRM ---
@router.callback_query(F.data.startswith("remove_"))
async def delete_selected_promo(callback: CallbackQuery):
    promo_id = int(callback.data.replace("remove_", ""))
    delete_promotion(promo_id)
    await callback.message.answer(f"✅ Aksiya (ID: {promo_id}) o‘chirildi.")
    await callback.answer()
