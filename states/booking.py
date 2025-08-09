from aiogram.fsm.state import State, StatesGroup


class Booking(StatesGroup):
    waiting_for_kottej_number = State()
    waiting_for_date = State()
    waiting_for_feedback = State()

