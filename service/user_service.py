from utils import SQLRepository
from dependency import file_data

import mimetypes
from fastapi import HTTPException


class UserService:
    def __init__(self):
        self.repo = SQLRepository()
    
    def create_user(self, user, photo:file_data):
        content = photo.file.read()
        get_type = mimetypes.guess_type(photo.filename)[0]
        extens_type = mimetypes.guess_extension(get_type) if get_type else None

        if extens_type not in ['.png','.jpg', '.jpeg']:
            raise HTTPException(422, "Incorect format photo")
        return self.repo.add_user(data=user, content=content)


    def get_one_user(self, username:str):
        if not username:
            raise HTTPException(400, "bad request")
        return self.repo.get_user_name(username)