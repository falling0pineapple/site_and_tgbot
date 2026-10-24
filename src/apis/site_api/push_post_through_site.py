from fastapi import APIRouter
from src.apis.site_api.schemas import PostModel
from src.database.queries.create_post import create_post
router = APIRouter()


@router.post("/push/post/in/tg/chanel")
def push_the_post_through_site(site_data: PostModel):
    return create_post(site_data.title, site_data.author)