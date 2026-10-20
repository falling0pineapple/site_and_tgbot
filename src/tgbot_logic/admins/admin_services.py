#here is service for queries to DataBase
from src.config import settings
from src.database.queries.get_suggested_posts import select_suggested_posts


def is_admin(current_user_id: int) -> bool:
    return current_user_id in settings.ADMINS_ID
    
    
    
def get_suggested_posts_SERVICE(current_user_id: int, limit: int):
    if is_admin(current_user_id):
        return select_suggested_posts(limit)
    return "None"