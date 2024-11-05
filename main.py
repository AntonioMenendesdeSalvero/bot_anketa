# bot.py
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from aiogram.fsm.storage.memory import MemoryStorage

# Ініціалізація бота та логера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Імпортуємо хендлери
from handlers import admin_handlers, profile_handlers, registration_handlers, general_handlers

# Додаємо роутери
dp.include_router(admin_handlers.router)
dp.include_router(profile_handlers.router)
dp.include_router(registration_handlers.router)
dp.include_router(general_handlers.router)

if __name__ == '__main__':
    dp.run_polling(bot)
