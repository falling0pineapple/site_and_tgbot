import asyncio
from aiogram import (Bot, Dispatcher as dp)
from src.config import settings

bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
