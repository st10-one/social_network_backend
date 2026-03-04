from fastapi import HTTPException, status

from utils import SQLRepository

class LikeService:
    def __init__(self):
        self.repo = SQLRepository()

    def create_like(self, likes):
        if not likes:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return self.repo.add_like(likes)