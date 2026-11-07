from sqlalchemy.orm import Mapped, mapped_column
from database.engine import Base
from sqlalchemy.types import VARCHAR
from sqlalchemy import DateTime, func
from datetime import datetime

#пока что только текст
class SuggestedPostORM(Base):
    __tablename__ = "suggested_posts"
    
    post_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(100))
    author: Mapped[str | None] = mapped_column()
    
    
class SuggestedPostArchiveORM(Base):
    __tablename__ = "archive_suggested_posts"
    
    post_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    title: Mapped[str] = mapped_column(VARCHAR(100))
    author: Mapped[str | None] = mapped_column()
    in_chanel: Mapped[bool] = mapped_column()
    deleted_at: Mapped[datetime]  = mapped_column(DateTime(timezone=True), server_default=func.now())