from schemas import PostsSchema
from fastapi import APIRouter, Depends

from service import PostService

router = APIRouter(prefix='/social')

@router.post('/add_post', tags=['Post'])
def add_posts(content: PostsSchema = Depends(), post_service:PostService = Depends()):
    return post_service.create_post(content=content)
