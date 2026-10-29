#here is service for queries to DataBase
from config import settings
from database.queries.get_suggested_posts import select_suggested_posts


def is_admin(current_user_id: int) -> bool:
    return current_user_id in settings.ADMINS_ID
    
    
    
def get_suggested_posts_SERVICE(current_user_id: int):
    if is_admin(current_user_id):
        return select_suggested_posts()
    return "None"