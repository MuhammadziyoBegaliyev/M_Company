from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from keyboards.inline import feedback_rating_kb
from aiogram.fsm.context import FSMContext
from states.feedback import FeedbackState
from database.db import add_feedback
from config import ADMINS

router = Router()

@router.callback_query(F.data == "feedback_start")  
async def start_feedback(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Xizmatni baholang:")
    await callback.message.answer("⭐️ Yulduzcha baho bering:", reply_markup=feedback_rating_kb())
    await state.set_state(FeedbackState.rating)

@router.callback_query(F.data.startswith("fb_"))
async def process_rating(callback: CallbackQuery, state: FSMContext, bot):
    rating = int(callback.data.split("_")[1])
    await state.update_data(rating=rating)
    await callback.message.edit_text("Rahmat! Endi qisqacha izoh qoldiring:")
    await state.set_state(FeedbackState.comment)

@router.message(FeedbackState.comment)
async def process_comment(message: Message, state: FSMContext, bot):
    data = await state.get_data()
    await add_feedback(message.from_user.id, data['rating'], message.text)
    await message.answer("✅ Fikringiz uchun rahmat!")
    for admin_id in ADMINS:
        await bot.send_message(admin_id, f"🔔 Yangi feedback!\nBaho: {data['rating']}\nIzoh: {message.text}")
    await state.clear()
