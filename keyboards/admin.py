

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def admin_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Bronlar ro‘yxati")],
            [KeyboardButton(text="➕ Aksiya qo‘shish"), KeyboardButton(text="🗑 Aksiyani o‘chirish")],
            [KeyboardButton(text="🔙 Ortga")]
        ],
        resize_keyboard=True
    )

def generate_promo_delete_keyboard(promotions):
    buttons = [
        [InlineKeyboardButton(text=f"{title}", callback_data=f"delete_promo_{promo_id}")]
        for promo_id, title, _ in promotions
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
