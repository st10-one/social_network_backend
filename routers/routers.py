from fastapi import APIRouter
from fastapi import Depends

from dependency import usr_data_dep, file_data
from schemas import PostsSchema, LikesSchema

from service import UserService, PostService, LikeService


router = APIRouter(prefix='/social')


@router.post('/add_new', tags=['Users'])
def add_users(user_data: usr_data_dep, Photo:file_data, user_service:UserService = Depends(UserService)): # type: ignore
    return user_service.create_user(user_data, Photo)


@router.get('/get_one_user/{username}', tags=['Users'])
def get_one_user(username: str, user_service:UserService = Depends(UserService)):
    return user_service.get_one_user(username=username)

@router.post('/add_post')
def add_posts(content: PostsSchema = Depends(), post_service:PostService = Depends(PostService)):
    return post_service.create_post(content=content)

@router.post('/add_like')
def add_like(like: LikesSchema = Depends(), like_service:LikeService = Depends()):
    return like_service.create_like(likes=like)