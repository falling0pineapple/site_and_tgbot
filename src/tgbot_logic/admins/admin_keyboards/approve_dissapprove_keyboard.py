from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def approve_disapprove_kb(id: int):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='approve', callback_data=f'approve_{id}')],
            [InlineKeyboardButton(text='disapprove', callback_data=f'disapprove_{id}')]
        ]
    )