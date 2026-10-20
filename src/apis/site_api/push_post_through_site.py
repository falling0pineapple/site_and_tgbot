from fastapi import APIRouter
from src.apis.site_api.schemas import PostModel
router = APIRouter()


@router.post("/push/post/in/tg/chanel")
def push_the_post_through_site(site_data: PostModel):
    ...