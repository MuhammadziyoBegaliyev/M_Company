from aiogram import Router, F
from aiogram.types import Message
from database.menu import add_menu_item, get_menu_items, delete_menu_item

router = Router()

ADMIN_IDS = [6824528065]

@router.message(F.text.startswith("/addfood"))
async def add_food(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Siz admin emassiz.")
        return

    parts = message.text.split("|")
    if len(parts) < 5:
        await message.answer("Format: /addfood | Kategoriya | Nomi | Tavsif | Narx")
        return

    _, category, name, desc, price = parts
    add_menu_item(category.strip(), name.strip(), desc.strip(), float(price))
    await message.answer(f"Yangi taom qo‘shildi: {name.strip()}")

@router.message(F.text == "📋 Menyu")
async def show_menu(message: Message):
    items = get_menu_items()
    if not items:
        await message.answer("Hozircha menyuda taomlar yo‘q.")
        return

    text = ""
    for item in items:
        text += f"<b>{item[2]}</b> ({item[1]})\n{item[3]}\nNarx: {item[4]} so‘m\n\n"

    await message.answer(text)

@router.message(F.text.startswith("/delfood"))
async def del_food(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Siz admin emassiz.")
        return

    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("Format: /delfood ID")
        return

    item_id = int(parts[1])
    delete_menu_item(item_id)
    await message.answer(f"Taom ID {item_id} o‘chirildi.")
