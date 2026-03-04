from utils import SQLRepository

from fastapi import HTTPException

class PostService:
    def __init__(self):
        self.repo = SQLRepository()

    def create_post(self, content):
        if not content:
            raise HTTPException(400, "bad request")
        return self.repo.add_posts(content)
