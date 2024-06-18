from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def user_menu():

    menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Передать клиента в работу")],
        [KeyboardButton(text="Как начать работу с нами?")]
    ], resize_keyboard=True)

    return menu
    

def menu_faq():
    menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Главное меню")],
        [KeyboardButton(text="Наша основная цель")],
        [KeyboardButton(text="Чем мы занимаемся?")],
        [KeyboardButton(text="Что от Вас требуеться")]
    ], resize_keyboard=True)
    return menu