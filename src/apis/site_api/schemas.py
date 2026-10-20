from pydantic import BaseModel

class PostModel(BaseModel):
    title: str
    author: str
    