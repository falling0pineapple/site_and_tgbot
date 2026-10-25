from aiogram import Router, F
from src.tgbot_logic.admins.admin_services import get_suggested_posts_SERVICE
from src.tgbot_logic.admins.admin_keyboards.approve_dissapprove_keyboard import approve_disapprove_kb
from src.database.queries.delete_post import delete_post_query
from src.config import settings
from src.database.queries.get_post_to_post import get_certain_suggested_post_query
router = Router()


@router.callback_query(F.data == "check_suggested_posts")
async def send_suggested_post_TG(callback):
    current_user_id = callback.from_user.id
    suggested_post = get_suggested_posts_SERVICE(current_user_id)
    if suggested_post is not None:
        await callback.message_answer(f"{suggested_post["description"]}\n\nAuthor: {suggested_post["author"]}",reply_markup=approve_disapprove_kb(suggested_post["post_id"]))
    else:
        await callback.message_answer(f"magic, nothing\n\n{suggested_post}")
    
@router.callback_query(F.data.startswith("approve_"))
async def post_post_in_chanel(callback):
    post_id = callback.data.replace('approve_', '')
    suggested_post = get_certain_suggested_post_query(post_id)
    await callback.bot.send_message(
        chat_id=settings.CHANEL_ID,
        text=suggested_post["description"]
        )
    if delete_post_query(post_id):
            current_user_id = callback.from_user.id
            suggested_postt = get_suggested_posts_SERVICE(current_user_id)
            if suggested_postt is not None:
                await callback.message_answer(f"{suggested_postt["description"]}\n\nAuthor: {suggested_postt["author"]}",reply_markup=approve_disapprove_kb(suggested_postt['post_id']))
    else:
        await callback.message_answer("PIPWRONG")
        
    
    
@router.callback_query(F.data.startswith("disapprove_"))
async def dissaprove_post_TG(callback):
    post_id = callback.data.replace("disaprove_", '')
    if delete_post_query(post_id):
        current_user_id = callback.from_user.id
        suggested_post = get_suggested_posts_SERVICE(current_user_id)
        if suggested_post is not None:
            await callback.message_answer(f"{suggested_post["description"]}\n\nAuthor: {suggested_post["author"]}",reply_markup=approve_disapprove_kb(suggested_post['post_id']))
    else:
            await callback.message_answer("PIPWRONG")
    
    
    #доделать approve часть
