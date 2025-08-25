# states/service_state.py
from aiogram.fsm.state import State, StatesGroup

class ServiceStates(StatesGroup):
    waiting_service_filter = State()
    waiting_location = State()
    browsing_results = State()
