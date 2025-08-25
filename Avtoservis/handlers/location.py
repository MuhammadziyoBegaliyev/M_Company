# handlers/location.py
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from states.service_state import ServiceStates
from utils.geo import find_nearby_providers
from database.db import PROVIDERS
from utils.helpers import result_actions_kb

router = Router()

@router.callback_query(F.data.startswith("filter:"))
async def filter_selected(callback: types.CallbackQuery, state: FSMContext):
    tag = callback.data.split(":")[1]
    await state.update_data(tag=tag)
    await state.set_state(ServiceStates.waiting_location)
    await callback.message.answer("📍 Iltimos, lokatsiyangizni yuboring", 
                                  reply_markup=types.ReplyKeyboardMarkup(
                                      keyboard=[[types.KeyboardButton(
                                          text="📍 Отправить локацию", request_location=True)]],
                                      resize_keyboard=True))
    await callback.answer()

@router.message(ServiceStates.waiting_location, F.location)
async def location_received(message: types.Message, state: FSMContext):
    data = await state.get_data()
    tag = data.get("tag")

    user_lat, user_lon = message.location.latitude, message.location.longitude
    nearby = find_nearby_providers(user_lat, user_lon, tag, limit=3)

    if not nearby:
        await message.answer("❌ Bu xizmat bo‘yicha yaqin servis topilmadi.")
        return

    await state.set_state(ServiceStates.browsing_results)
    await state.update_data(results=nearby, index=0)

    provider, dist = nearby[0]
    await message.answer_photo(photo=provider.photo_url,
                               caption=f"🏪 <b>{provider.name}</b>\n📍 {dist:.1f} km\nℹ️ {provider.info}",
                               reply_markup=result_actions_kb(provider, has_next=len(nearby) > 1))
