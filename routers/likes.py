from schemas import LikesSchema
from fastapi import APIRouter, Depends

from service import LikeService

router = APIRouter(prefix="/social")


@router.post("/like", tags=["Like"])
def add_like(like: LikesSchema = Depends(), like_service: LikeService = Depends()):
    return like_service.create_like(likes=like)


@router.delete("/like", tags=["Like"])
def delete_like(like: LikesSchema = Depends(), like_service: LikeService = Depends()):
    return like_service.delete_like(like)
