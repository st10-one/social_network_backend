from utils import users
from db import UsersModel

import mimetypes
from fastapi import HTTPException


class UserService:
    def __init__(self):
        self.repo = users.UserRepository()

    def create_user(self, user: UsersModel) -> UsersModel:
        return self.repo.add_user(data=user)

    def get_one_user(self, username: str):
        if not username:
            raise HTTPException(400, "bad request")
        return self.repo.get_user_name(username)

    def update_data(self, user_id: int, data: UsersModel) -> UsersModel:
        return self.repo.update_user(user_id=user_id, data=data)

    def delete_user(self, user_id: int):
        return self.repo.delete_user(user_id)
