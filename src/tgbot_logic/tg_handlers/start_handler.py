from aiogram import Router, F
from aiogram.filters import Command

router=Router()


@router.message(Command("start"))
async def start_bot_handler(message):
    await message.answer("PIP")
