
from aiogram import Router, F
from aiogram.types import Message
from database.tarifs import add_tarif, get_tarifs, delete_tarif

router = Router()

ADMIN_IDS = [6824528065]  # o‘zgartir: admin ID

@router.message(F.text.startswith("/addtarif"))
async def add_tarif_handler(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Siz admin emassiz.")
        return

    parts = message.text.split("|")
    if len(parts) < 4:
        await message.answer("Format: /addtarif | Nomi | Tavsif | Narx")
        return

    _, name, desc, price = parts
    add_tarif(name.strip(), desc.strip(), float(price))
    await message.answer(f"Tarif qo‘shildi: {name.strip()}")

@router.message(F.text.startswith("/tariflist"))
async def tarif_list(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Siz admin emassiz.")
        return

    tarifs = get_tarifs()
    if not tarifs:
        await message.answer("Tariflar yo‘q.")
        return

    text = "\n".join([f"{tid}: {name} - {price} so‘m" for tid, name, desc, price in tarifs])
    await message.answer(f"Tariflar:\n{text}")

@router.message(F.text.startswith("/deltarif"))
async def del_tarif_handler(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("Siz admin emassiz.")
        return

    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("Format: /deltarif ID")
        return

    tarif_id = int(parts[1])
    delete_tarif(tarif_id)
    await message.answer(f"Tarif ID {tarif_id} o‘chirildi.")

@router.message(F.text == "🏷️ Maxsus tariflar")
async def show_tarifs(message: Message):
    tarifs = get_tarifs()
    if not tarifs:
        await message.answer("Hozircha maxsus tariflar yo‘q.")
        return

    text = ""
    for tarif in tarifs:
        text += f"<b>{tarif[1]}</b>\n{tarif[2]}\nNarxi: {tarif[3]} so‘m\n\n"

    await message.answer(text)
