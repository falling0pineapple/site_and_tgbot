from aiogram import Router, F
from src.config import settings
from tgbot_logic.admins.admin_keyboards.main_admin_keyboard import main_admin_keyboard
router = Router()


@router.message(F.text == "/admin")
async def main_admin_panel(message):
    current_user = message.from_user.id
    if current_user not in settings.ADMINS_ID:
        await message.answer("You are not admin!")
    await message.answer("You are in admin mode!", reply_markup=main_admin_keyboard())