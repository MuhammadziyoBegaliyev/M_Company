from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def phone_request_kb():
    """
    Telefon raqam so‘rash tugmasi
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📞 Telefon raqam yuborish", request_contact=True)]
        ],
        resize_keyboard=True
    )


def register_language_kb():
    """
    Tilni tanlash tugmalari
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇷🇺 Русский")]
        ],
        resize_keyboard=True
    )


def main_menu_kb(lang="uz"):
    """
    Asosiy menyu — foydalanuvchi tiliga qarab.
    """
    if lang == "ru":
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🏠 Бронирование")],
                [KeyboardButton(text="📋 Меню")],
                [KeyboardButton(text="📍 Локация")],
                [KeyboardButton(text="☎️ Контакт"), KeyboardButton(text="🎉 Акции")],
                [KeyboardButton(text="🏷️ Специальные тарифы")],
                [KeyboardButton(text="🌐 Сменить язык")]
            ],
            resize_keyboard=True
        )
    else:  # default: uzbek
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🏠 Bron qilish")],
                [KeyboardButton(text="📋 Menyu")],
                [KeyboardButton(text="📍 Lokatsiya")],
                [KeyboardButton(text="☎️ Murojaat"), KeyboardButton(text="🎉 Aksiyalar")],
                [KeyboardButton(text="🏷️ Maxsus tariflar")],
                [KeyboardButton(text="🌐 Tilni o'zgartirish")]
            ],
            resize_keyboard=True
        )
