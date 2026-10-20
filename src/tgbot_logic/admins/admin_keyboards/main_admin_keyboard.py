from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_admin_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Check suggested posts', callback_data='check_suggested_posts')],
            [InlineKeyboardButton(text='Quit the admin mode', callback_data='quit_admin_mode')], #не представляю как я это буду реализовывать
        ]
    )