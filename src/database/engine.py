from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.config import settings



sync_engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)

session_factory = sessionmaker(sync_engine)

class Base(DeclarativeBase):
    pass

#made orm
def create_base():
    from src.database import models
    Base.metadata.create_all(bind=sync_engine)