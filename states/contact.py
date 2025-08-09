

from aiogram.fsm.state import StatesGroup, State

class ContactForm(StatesGroup):
    name = State()
    phone = State()
    message = State()
