from aiogram.fsm.state import State, StatesGroup


class AddLeadUser(StatesGroup):
    phone_client = State()
    city = State()
    name = State()
    comment_client = State()
