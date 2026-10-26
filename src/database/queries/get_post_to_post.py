from sqlalchemy import select
from src.database.models import SuggestedPostORM
from src.database.engine import session_factory

def get_certain_suggested_post_query(post_id: int):
    with session_factory() as session:
        query = select(SuggestedPostORM).where(SuggestedPostORM.post_id == post_id)
        result = session.scalar(query)
        if result:
            post = {
                "post_id": result.post_id,
                "description": result.title,
                "author": result.author
            }
            return post
        return None