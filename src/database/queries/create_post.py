from src.database.models import SuggestedPostORM
from src.database.engine import session_factory


def create_post(title: str, author: str):
    with session_factory() as session:
        session.add(SuggestedPostORM(title=title, author=author))
        session.commit()
        return "post created"
