import sqlite3
from fastapi import HTTPException


from db import PostModel
from .parents_class import AbstractPostRepository
from .conf import FOREIGN_KEY, PATH_HOME


class PostRepository(AbstractPostRepository):
    def __init__(self):
        self.conn = sqlite3.connect(
            f"{PATH_HOME}/vs_code/social_network_backend/database/data.db", check_same_thread=False
        )
        self.cursor = self.conn.cursor()
    
    def add_posts(self, data: PostModel):
        params = (data.user_id, data.content)

        try:
            self.cursor.execute(FOREIGN_KEY)
            self.cursor.execute(
                "INSERT INTO Posts(user_id, content) VALUES (?,?)", params
            )
            self.conn.commit()
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(400, "bad request")

        return {"id": data.user_id, "content": data.content}

    def delete_post(self, user_id: int):
        try:
            self.cursor.execute(FOREIGN_KEY)
            self.cursor.execute("DELETE FROM Posts where user_id = ?", (user_id,))
            self.conn.commit()
        except sqlite3.Error,TypeError:
            self.conn.rollback()
            raise HTTPException(400, "bad request")
        
        return {"user_id": user_id}
