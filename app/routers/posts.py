from schemas import PostsSchema
from fastapi import APIRouter, Depends

from service import PostService

router = APIRouter(prefix="/social/v1")


@router.post("/post", tags=["Posts"])
async def add_posts(content: PostsSchema = Depends(), post_service: PostService = Depends()):
    return post_service.create_post(content=content)


@router.delete("/post", tags=["Posts"])
async def delete_post(user_id: int, post_service: PostService = Depends()):
    return post_service.delete_post(user_id)
