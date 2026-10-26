from src.database.models import SuggestedPostORM
from src.database.engine import session_factory
from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError

def delete_post_query(post_id: int):
    with session_factory() as session:
        query = delete(SuggestedPostORM).where(SuggestedPostORM.post_id == post_id)
        result = session.execute(query)
        if result.rowcount() >= 1:
            session.commit()
            return 'delete'
        raise SQLAlchemyError