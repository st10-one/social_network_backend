import sqlite3
from typing import Annotated

from fastapi import APIRouter, UploadFile
from fastapi import Depends, File

from .depends import user_data
from .schemas import UsersSchema, PostsSchema, LikesSchema

from utils import SQLRepository
from .depends import sql_conn

from service import vallidation_type

sql_dep = Annotated[sqlite3.Connection, Depends(sql_conn)]
file_data = Annotated[UploadFile, File()]
usr_data_dep = Annotated[UsersSchema, Depends(user_data)]


router = APIRouter(prefix='/social')


@router.post('/add_new', tags=['Users'])
def add_users(user_data: usr_data_dep, Photo:file_data, repository: SQLRepository = Depends()):
    vallidation_type(Photo.filename)
    content = Photo.file.read()
    repository.add_user(user_data, content)
    return {"userdata": user_data}


@router.get('/get_one_user/{username}', tags=['Users'])
def get_one_user(username: str, repository: SQLRepository = Depends()):
    res = repository.get_user_name(username)
    return {"data": res}

@router.post('/add_post')
def add_posts(content: PostsSchema = Depends(), repository: SQLRepository = Depends()):
    repository.add_posts(content)
    return {
        "user_id": content.user_id,
        "content": content.content
    }

@router.post('/add_like')
def add_like(likes: LikesSchema = Depends(), repository: SQLRepository = Depends()):
    repository.add_like(likes)
    return {
        "user_id": likes.user_id,
        "post_id": likes.post_id
    }