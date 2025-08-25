from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Avtoservis xizmatlari ro'yxati (Rus tilida)
SERVICE_FILTERS = [
    ("Электрик", "elektrik"),
    ("Кастоправ", "kastoprav"),
    ("Мотариус", "motarius"),
    ("Вулканизация", "vulkanizatsiya"),
    ("Развал-схождение", "razval"),
    ("Тонировка", "tonirovka"),
    ("Шумоизоляция", "shumka"),
    ("Универсал мастер", "universal"),
    ("Автомойка", "avtomoyka"),
    ("Замена масла", "oil_change"),
    ("Диагностика", "diagnostika"),
    ("Кондиционер", "konditsioner"),
    ("Ходовая часть", "hodovaya"),
    ("Кузовной ремонт", "kuzov"),
    ("Покраска", "pokraska"),
    ("Слесарь", "slesar"),
]

def services_filter_kb() -> InlineKeyboardMarkup:
    """
    Автосервис фильтр клавиатура
    Inline tugmalar orqali xizmatlarni chiqaradi
    """
    buttons = [
        InlineKeyboardButton(
            text=title,
            callback_data=f"service:{tag}:{title}"  # callback_data: service:oil_change:Замена масла
        )
        for title, tag in SERVICE_FILTERS
    ]

    # Har qatorga 2 tadan tugma joylashtirish
    rows = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]

    # Pastki boshqaruv tugmalari
    rows.append([
        InlineKeyboardButton(text="⬅️ Назад", callback_data="back:menu"),
        InlineKeyboardButton(text="🏠 Главное меню", callback_data="back:main")
    ])

    return InlineKeyboardMarkup(inline_keyboard=rows)
