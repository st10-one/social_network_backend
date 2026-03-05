from utils import SQLRepository
from db import PostModel

class PostService:
    def __init__(self):
        self.repo = SQLRepository()

    def create_post(self, content:PostModel) -> PostModel:
        return self.repo.add_posts(content)
