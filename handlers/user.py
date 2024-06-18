from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from handlers.func import *
from keyboard.text import *
import keyboard.reply as kb
from utils.user_state import AddLeadUser

user = Router()


@user.message(CommandStart())
async def start(m: Message):
    await m.answer(main_text, reply_markup=kb.user_menu())


@user.message(F.text == 'Передать клиента в работу')
async def add_client_user(m: Message, state:  FSMContext):
    await m.answer(add_client)
    await state.set_state(AddLeadUser.phone_client)
    await m.answer("Введите номер телефона клиента")


@user.message(F.text == 'Как начать работу с нами?')
async def faq(m: Message):
    await m.answer("Открываю меню \"Как начать работу с нами\"", reply_markup=kb.menu_faq())


@user.message(F.text == 'Главное меню')
async def main_menu(m: Message):
    await m.answer(main_text, reply_markup=kb.user_menu())


@user.message(F.text == 'Наша основная цель')
async def main_goal(m: Message):
    await m.answer(text_kb)
       

@user.message(F.text == 'Чем мы занимаемся?')
async def main_two(m: Message):
    await m.answer(text_kb_two)


@user.message(F.text == 'Что от Вас требуеться')
async def main_three(m: Message):
    await m.answer(text_kb_three)


@user.message(AddLeadUser.phone_client)
async def load_phone_client(m: Message, state: FSMContext):
    if not m.text.startswith('+7') and not m.text.startswith('89'):
        await m.answer("Номер должен начинаться с +7 либо 89")

    elif m.text == '+79111234567/Комментарий':
        await m.answer("Такой лид уже есть в нашей базе данных")

    else:
        await state.update_data(phone=m.text)
        await m.answer("Введите город")
        await state.set_state(AddLeadUser.city)


@user.message(AddLeadUser.city)
async def load_city(m: Message, state: FSMContext):
    await state.update_data(city=m.text)
    await m.answer("Введите имя")
    await state.set_state(AddLeadUser.name)


@user.message(AddLeadUser.name)
async def load_name(m: Message, state: FSMContext):
    await state.update_data(name=m.text)
    await m.answer("Введите комментарий")
    await state.set_state(AddLeadUser.comment_client)


@user.message(AddLeadUser.comment_client)
async def load_comment_client(m: Message, state: FSMContext):
    username = m.from_user.username
    full_name = m.from_user.full_name
    data = await state.get_data()
    name = f"@{username}" if username != None else full_name

    id = await create_contact(name=data['name'],  client_phone=data['phone'])
    res = await add_lead(cnt_id=id, name_client=data['name'], comment=m.text,
                   client_phone=data['phone'], city=data['city'], name=name)
    await state.clear()

    if res:
        await m.answer("Лид успешно добавлен")
    else:
        await m.answer("Ошибка при добавлении лида")
