from database.models import SuggestedPostORM
from database.engine import session_factory
from sqlalchemy import select

def select_suggested_posts():
    with session_factory() as session:
        len_query = session.query(SuggestedPostORM).count()
        query = select(SuggestedPostORM)
        result = session.scalars(query).first()
        if result is None:
            return None
        post = {
            "post_id": result.post_id,
            "description": result.title,
            "author": result.author,
            "lenght": len_query
        }
        return post