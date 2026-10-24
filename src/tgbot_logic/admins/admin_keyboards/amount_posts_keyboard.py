from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def amount_of_posts_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='1', callback_data='1')],
            [InlineKeyboardButton(text='1', callback_data='5')],
            [InlineKeyboardButton(text='1', callback_data='10')],
        ]
    )
    
    
#он не надо теперь