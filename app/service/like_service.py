from db import LikesModel

from utils import likes


class LikeService:
    def __init__(self):
        self.repo = likes.LikeRepository()

    def create_like(self, likes: LikesModel) -> LikesModel:
        return self.repo.add_like(likes)

    def delete_like(self, likse: LikesModel) -> LikesModel:
        return self.repo.delete_like(likse)
