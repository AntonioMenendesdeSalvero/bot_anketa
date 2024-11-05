# handlers/registration_handlers.py
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from database import add_user, get_user
import logging
from aiogram import F
from keyboards import get_reply_keyboard, get_profile_inline_keyboard, get_admin_inline_keyboard


router = Router()
logger = logging.getLogger(__name__)

from aiogram.fsm.state import StatesGroup, State

class RegistrationStates(StatesGroup):
    photo = State()
    description = State()
    price = State()
    seminar_link = State()
    phone_number = State()

@router.message(F.text == 'Подати інформацію про себе')
async def registration_btn(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if get_user(user_id):
        await message.answer("Ваша анкета вже прийнята! Для того, щоб переглянути її, перейдіть у розділ 'Профіль'.")
    else:
        await message.answer("Надішліть своє фото для реєстрації.")
        await state.set_state(RegistrationStates.photo)
    logger.info(f"Registration process started by user {user_id}")

# Додаткові хендлери реєстрації тут
