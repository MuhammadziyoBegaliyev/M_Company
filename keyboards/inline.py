from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_inline_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang_uz"),
         InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_main")]
    ])


def booking_menu_kb():
    kb = [
        [InlineKeyboardButton(text="🏠 Kottej", callback_data="book_kottej")],
        [InlineKeyboardButton(text="🛋 Tapchan", callback_data="book_tapchan")],
        [InlineKeyboardButton(text="🏊 Basseyn", callback_data="book_basseyn")],
        [InlineKeyboardButton(text="🧖 Sauna", callback_data="book_sauna")],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="go_back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


def kottej_number_kb():
    kb = [
        [InlineKeyboardButton(text=str(i), callback_data=f"kottej_{i}")]
        for i in range(1, 9)
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


def add_more_kb():
    kb = [
        [InlineKeyboardButton(text="🏠 Kottej", callback_data="book_kottej")],
        [InlineKeyboardButton(text="🛋 Tapchan", callback_data="book_tapchan")],
        [InlineKeyboardButton(text="🏊 Basseyn", callback_data="book_basseyn")],
        [InlineKeyboardButton(text="🧖 Sauna", callback_data="book_sauna")],
        [InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="confirm_booking")],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="go_back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)




###admin panel


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# 🔧 Admin panel tugmalari
def admin_panel_kb():
    kb = [
        [InlineKeyboardButton(text="➕ Aksiya qo'shish", callback_data="add_promotion")],
        [InlineKeyboardButton(text="🗑 Aksiya o'chirish", callback_data="delete_promotion")],
        [InlineKeyboardButton(text="🏷 Maxsus tarif qo'shish", callback_data="add_special_tarif")],
        [InlineKeyboardButton(text="📜 Barcha bronlar", callback_data="all_bookings")],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="admin_back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


# ➕ Aksiya qo'shishdan keyin tasdiqlash tugmasi
def confirm_add_promotion_kb():
    kb = [
        [InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="confirm_add_promotion")],
        [InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel_add_promotion")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


# 🗑 Aksiya o‘chirish tugmalari (dinamik ravishda promo ID ga qarab generatsiya qilinadi)
def delete_promotion_kb(promotions: list[tuple]):
    """
    promotions: list of tuples (promo_id, promo_title)
    """
    kb = []
    for promo_id, title in promotions:
        kb.append([InlineKeyboardButton(text=f"🗑 {title}", callback_data=f"delete_promotion_{promo_id}")])
    kb.append([InlineKeyboardButton(text="⬅️ Orqaga", callback_data="admin_back")])
    return InlineKeyboardMarkup(inline_keyboard=kb)


# 🏷 Maxsus tarif qo‘shish tugmasidan keyin tasdiqlash
def confirm_add_tarif_kb():
    kb = [
        [InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="confirm_add_tarif")],
        [InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel_add_tarif")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)


# 📜 Barcha bronlar tugmasidan keyin qaytish
def back_to_admin_kb():
    kb = [
        [InlineKeyboardButton(text="⬅️ Admin panelga qaytish", callback_data="admin_back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)






###
def back_admin_kb():
    kb = [[InlineKeyboardButton(text="⬅️ Orqaga", callback_data="admin_back")]]
    return InlineKeyboardMarkup(inline_keyboard=kb)



def feedback_rating_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⭐", callback_data="fb_1"),
         InlineKeyboardButton(text="⭐⭐", callback_data="fb_2"),
         InlineKeyboardButton(text="⭐⭐⭐", callback_data="fb_3"),
         InlineKeyboardButton(text="⭐⭐⭐⭐", callback_data="fb_4"),
         InlineKeyboardButton(text="⭐⭐⭐⭐⭐", callback_data="fb_5")]
    ])




def location_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📍 Xaritani ochish",
                    url="https://www.google.com/maps/place/%D0%90%D0%BC%D0%B8%D1%80+%D0%A2%D0%B5%D0%BC%D1%83%D1%80+%D0%A5%D0%B8%D0%B5%D0%B1%D0%BE%D0%BD%D0%B8/@41.3153097,69.2953007,14z/data=!4m6!3m5!1s0x38ae8b2c64aa3d0f:0xba59bc80197d4da8!8m2!3d41.312765!4d69.283501!16s%2Fm%2F0jwtkyq?entry=ttu&g_ep=EgoyMDI1MDcyOS4wIKXMDSoASAFQAw%3D%3D"
                )
            ]
        ]
    )


def contact_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💬 Operator bilan bog‘lanish",
                    url="https://t.me/Muhammadziyo7008"
                )
            ]
        ]
    )
