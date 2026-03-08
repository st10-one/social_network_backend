from utils import SQLRepository
from dependency import file_data
from db import UsersModel

import mimetypes
from fastapi import HTTPException


class UserService:
    def __init__(self):
        self.repo = SQLRepository()

    def create_user(self, user: UsersModel, photo: file_data) -> UsersModel:
        content = photo.file.read()
        get_type = mimetypes.guess_type(photo.filename)[0]
        extens_type = mimetypes.guess_extension(get_type) if get_type else None

        if extens_type not in [".png", ".jpg", ".jpeg"]:
            raise HTTPException(422, "Incorect format photo")
        return self.repo.add_user(data=user, content=content)

    def get_one_user(self, username: str):
        if not username:
            raise HTTPException(400, "bad request")
        return self.repo.get_user_name(username)

    def update_data(self, user_id: int, data: UsersModel) -> UsersModel:
        return self.repo.update_user(user_id=user_id, data=data)

    def delete_user(self, user_id: int):
        return self.repo.delete_user(user_id)
