# handlers/contact.py

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.contact import ContactForm
from database.contacts import add_contact
from keyboards.contact import request_phone_kb, back_menu_kb

router = Router()

ADMIN_IDS = [6824528065]  # O‘zgartir: Admin Telegram ID


@router.message(F.text == "📩 Murojaat")
@router.message(F.text == "/contact")
async def start_contact(message: Message, state: FSMContext):
    await state.set_state(ContactForm.name)
    await message.answer("👤 Ismingizni kiriting:", reply_markup=back_menu_kb())


@router.message(ContactForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ContactForm.phone)
    await message.answer("📞 Telefon raqamingizni yuboring:", reply_markup=request_phone_kb)


@router.message(ContactForm.phone, F.contact)
async def get_phone(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    await state.update_data(phone=phone)
    await state.set_state(ContactForm.message)
    await message.answer("✏️ Murojaatingizni yozib yuboring:")


@router.message(ContactForm.phone)
async def get_phone_text(message: Message, state: FSMContext):
    # Telefon raqamni matn orqali kiritgan bo‘lsa
    phone = message.text
    await state.update_data(phone=phone)
    await state.set_state(ContactForm.message)
    await message.answer("✏️ Murojaatingizni yozib yuboring:")


@router.message(ContactForm.message)
async def get_message(message: Message, state: FSMContext, bot):
    data = await state.get_data()
    user_id = message.from_user.id
    name = data['name']
    phone = data['phone']
    msg = message.text

    # Bazaga saqlash
    add_contact(user_id, name, phone, msg)

    # Adminga yuborish
    text = (
        f"📩 <b>Yangi murojaat:</b>\n\n"
        f"<b>Ism:</b> {name}\n"
        f"<b>Tel:</b> {phone}\n"
        f"<b>Xabar:</b> {msg}"
    )
    for admin_id in ADMIN_IDS:
        await bot.send_message(admin_id, text)

    await message.answer("✅ Murojaatingiz yuborildi!", reply_markup=None)
    await state.clear()


# Ortga tugma
@router.callback_query(F.data == "back_to_main")
async def back_to_main(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer("🏠 Asosiy menyuga qaytdingiz.", reply_markup=None)
