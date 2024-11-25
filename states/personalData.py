from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    fullname = State()
    username = State()
    phoneNumber = State()
    course = State()
    teacher = State()
    day = State()
    selected_time = State()
    confirm = State()