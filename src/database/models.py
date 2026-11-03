from sqlalchemy.orm import Mapped, mapped_column
from database.engine import Base
from sqlalchemy.types import VARCHAR


#пока что только текст
class SuggestedPostORM(Base):
    __tablename__ = "suggested_posts"
    
    post_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(100))
    author: Mapped[str | None] = mapped_column()