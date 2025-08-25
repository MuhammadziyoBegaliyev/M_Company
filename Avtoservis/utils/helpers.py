# utils/helpers.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.db import Provider

def gmaps_link(lat: float, lon: float) -> str:
    return f"https://maps.google.com/?q={lat},{lon}"

def tel_link(phone: str) -> str:
    return f"tel:{phone}"

def result_actions_kb(provider: Provider, has_next: bool) -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(text="📞 Позвонить", url=tel_link(provider.phone)),
            InlineKeyboardButton(text="📍 Локация", url=gmaps_link(provider.lat, provider.lon)),
        ]
    ]
    if has_next:
        rows.append([InlineKeyboardButton(text="⏭ Следующий", callback_data="next")])
    return InlineKeyboardMarkup(inline_keyboard=rows)
