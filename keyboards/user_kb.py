from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb(lang):
    if lang == "ru":
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🏠 Бронирование"), KeyboardButton(text="📖 Меню")],
                [KeyboardButton(text="📍 Локация"), KeyboardButton(text="📞 Контакты")],
                [KeyboardButton(text="🎉 Акции"), KeyboardButton(text="⭐ Спец тарифы")]
            ], resize_keyboard=True
        )
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏠 Bron qilish"), KeyboardButton(text="📖 Menyu")],
            [KeyboardButton(text="📍 Lokatsiya"), KeyboardButton(text="📞 Murojaat")],
            [KeyboardButton(text="🎉 Aksiyalar"), KeyboardButton(text="⭐ Maxsus tariflar")]
        ], resize_keyboard=True
    )
