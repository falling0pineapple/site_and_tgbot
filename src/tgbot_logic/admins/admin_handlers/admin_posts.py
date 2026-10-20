from aiogram import Router, F
from src.tgbot_logic.admins.admin_keyboards.amount_posts_keyboard import amount_of_posts_keyboard
from src.tgbot_logic.admins.admin_services import get_suggested_posts_SERVICE

router = Router()


@router.callback_query(F.data == "check_suggested_posts")
async def check_suggested_posts_what_amount(callback):
    await callback.message.edit_text("Choose amount of posts", reply_markup=amount_of_posts_keyboard())

    

@router.callback_query(F.data in ("1", "5", "10"))
async def send_suggested_posts(callback):
    current_user_id = callback.from_user.id
    limit = int(callback.data) 
    suggested_posts = get_suggested_posts_SERVICE(current_user_id, limit)
    for post in suggested_posts:
        await callback.message_answer(f"{post}") #сделать клавиатуру approve/disapprove
    await callback.message_answer("\nIt's all")
    
