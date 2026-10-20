from src.database.models import SuggestedPostORM
from src.database.engine import session_factory
from sqlalchemy import select

def select_suggested_posts(limit: int):
    with session_factory() as session:
        query = select(SuggestedPostORM).limit(limit)
        result = session.scalars(query).all()
        return result