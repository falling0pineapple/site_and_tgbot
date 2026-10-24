from src.database.models import SuggestedPostORM
from src.database.engine import session_factory
from sqlalchemy import delete

def delete_post_query(post_id: int):
    with session_factory() as session:
        query = delete(SuggestedPostORM).where(SuggestedPostORM.post_id == post_id)
        session.execute(query)
        session.commit()
        return 'delete'