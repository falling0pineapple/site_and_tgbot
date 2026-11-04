from aiogram import Router, F
from tgbot_logic.admins.admin_services import get_suggested_posts_SERVICE
from tgbot_logic.admins.admin_keyboards.approve_dissapprove_keyboard import approve_disapprove_kb
from database.queries.delete_post import delete_post_query
from config import settings
from database.queries.get_post_to_post import get_certain_suggested_post_query
router = Router()


@router.callback_query(F.data == "check_suggested_posts")
async def send_suggested_post_TG(callback):
    current_user_id = callback.from_user.id
    suggested_post = get_suggested_posts_SERVICE(current_user_id)
    if suggested_post is not None:
        await callback.message.answer(f"{suggested_post["description"]}\n\nAuthor: {suggested_post["author"]}",reply_markup=approve_disapprove_kb(suggested_post["post_id"]))
    elif suggested_post is None:
        await callback.message.answer("There are no posts")
    else:
        await callback.message.answer(f"magic, nothing\n\n{suggested_post}")
    
@router.callback_query(F.data.startswith("approve_"))
async def post_post_in_chanel(callback):
    print(f'CALLBACK DATA:: :: {callback.data}')
    post_id = int(callback.data.replace('approve_', ''))
    suggested_post = get_certain_suggested_post_query(post_id)
    await callback.bot.send_message(
        chat_id=settings.CHANEL_ID,
        text=suggested_post["description"]
        )
    if delete_post_query(post_id):
            current_user_id = callback.from_user.id
            suggested_postt = get_suggested_posts_SERVICE(current_user_id)
            if suggested_postt is not None:
                await callback.message.edit_text(f"{suggested_postt["description"]}\n\nAuthor: {suggested_postt["author"]}",reply_markup=approve_disapprove_kb(suggested_postt['post_id']))
            elif suggested_postt is None:
                await callback.message.edit_text("There are no posts")
            else:
                await callback.message.answer('pipiwrong')
    else:
        await callback.message.edit_text("PIPWRONG")
        
    
    
@router.callback_query(F.data.startswith("disapprove_"))
async def dissaprove_post_TG(callback):
    post_id = int(callback.data.replace("disapprove_", ''))
    if delete_post_query(post_id):
        current_user_id = callback.from_user.id
        suggested_post = get_suggested_posts_SERVICE(current_user_id)
        if suggested_post is not None:
            await callback.message.edit_text(f"{suggested_post["description"]}\n\nAuthor: {suggested_post["author"]}",reply_markup=approve_disapprove_kb(suggested_post['post_id']))
        elif suggested_post is None:
                await callback.message.edit_text("There are no posts")
        else:
            await callback.message.answer('pipiwrong')
    else:
            await callback.message.edit_text("PIPWRONG")
