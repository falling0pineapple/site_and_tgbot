from aiogram import Router, F
from src.config import settings
from tgbot_logic.admins.admin_keyboards.main_admin_keyboard import main_admin_keyboard
router = Router()


@router.message(F.text == "/admin")
async def main_admin_panel(message):
    current_user = message.from_user.id
    if current_user in settings.ADMINS_ID:
        await message.answer('admin mode!', main_admin_keyboard())
    if current_user not in settings.ADMINS_ID:
        await message.answer('you are not admin')