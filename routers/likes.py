from schemas import LikesSchema
from fastapi import APIRouter, Depends

from service import LikeService

router = APIRouter(prefix="/social/v1")


@router.post("/like", tags=["Likes"])
def add_like(like: LikesSchema = Depends(), like_service: LikeService = Depends()):
    return like_service.create_like(likes=like)


@router.delete("/like", tags=["Likes"])
def delete_like(like: LikesSchema = Depends(), like_service: LikeService = Depends()):
    return like_service.delete_like(like)
