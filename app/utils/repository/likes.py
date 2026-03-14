from .parents_class import AbstractLikeRepository
from db import LikesModel
from .conf import FOREIGN_KEY, PATH_HOME


from fastapi import HTTPException 
import sqlite3


class LikeRepository(AbstractLikeRepository):
    def __init__(self):
        self.conn = sqlite3.connect(
            f"{PATH_HOME}/social_network_backend/database/data.db", check_same_thread=False
        )
        self.cursor = self.conn.cursor()
    
    def add_like(self, data: LikesModel):
        params = (data.user_id, data.post_id)

        try:
            self.cursor.execute(FOREIGN_KEY)
            self.cursor.execute(
                "INSERT INTO Likes(user_id, post_id) VALUES (?,?)", params
            )
            self.conn.commit()
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(400, "bad request")

        return {"user_id": data.user_id, "post_id": data.post_id}

    def delete_like(self, data: LikesModel) -> LikesModel:
        params = (data.user_id, data.post_id)

        try:
            self.cursor.execute(FOREIGN_KEY)
            self.cursor.execute(
                "DELETE FROM Likes where user_id = ? and post_id = ?", params
            )
            self.conn.commit()
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(400, "bad request")

        return {"uses_id": data.user_id, "post_id": data.post_id}
