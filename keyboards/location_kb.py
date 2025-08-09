from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def location_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📍 Xaritani ochish", url="https://goo.gl/maps/YOUR_MAP_LINK")]
        ]
    )
