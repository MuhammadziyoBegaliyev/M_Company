# keyboards/reply.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Автосервисы")],  # <<< shu joyni o‘zgartirdik
    ],
    resize_keyboard=True
)
