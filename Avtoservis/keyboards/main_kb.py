# keyboards/main_kb.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

MAIN_MENU = [
    "Автосервисы",
    "Эвакуатор",
    "Бензин доставка",
    "Антиблокировка",
]

def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=MAIN_MENU[0]), KeyboardButton(text=MAIN_MENU[1])],
            [KeyboardButton(text=MAIN_MENU[2]), KeyboardButton(text=MAIN_MENU[3])],
            [KeyboardButton(text=MAIN_MENU[4])]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
