from aiogram.fsm.state import StatesGroup, State

class FeedbackState(StatesGroup):
    rating = State()
    comment = State()
