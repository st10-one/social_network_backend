from abc import ABC, abstractmethod
import sqlite3

from fastapi import HTTPException

from db import (
    UsersModel,
    PostModel,
    LikesModel
)

FOREIGN_KEY = "PRAGMA foreign_keys = ON;"

class AbstractRepository(ABC):
    @abstractmethod
    def add_user():
        raise NotImplemented
    
    @abstractmethod
    def get_user_name():
        raise NotImplemented
    
    @abstractmethod
    def add_posts():
        raise NotImplemented

    @abstractmethod
    def add_like():
        raise NotImplemented

class SQLRepository(AbstractRepository):
    def __init__(self):
        with sqlite3.connect('/home/stipa/database/data.db', check_same_thread=False) as conn:
            self.conn = conn
            self.cursor = conn.cursor()



    def add_user(self, data: UsersModel, content):
        params = (
            data.first_name, data.last_name,
            data.username, data.bio,
            content
        )

        try:
            self.cursor.execute("INSERT INTO Users(first_name, last_name, username, bio, photo_profil) VALUES (?,?,?,?,?)", params)
            self.conn.commit()
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(status_code=400, detail=f"user with this name exist\n")


    def get_user_name(self, name: str):
        try:
            self.cursor.execute("SELECT first_name, last_name, username FROM Users Where username = ? or first_name = ?", (name, name,))
            result = self.cursor.fetchone()
            return result
        except sqlite3.Error, TypeError:
            raise HTTPException(404, "not found")
        
        
    def add_posts(self, data: PostModel):
        params = (
            data.user_id, data.content
        )

        try:
            self.cursor.execute(FOREIGN_KEY)
            self.cursor.execute("INSERT INTO Posts(user_id, content) VALUES (?,?)", params)
            self.conn.commit()
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(400, "bad request")
        

    def add_like(self, data:LikesModel):
        params = (
            data.user_id, data.post_id
        )

        try:
            self.cursor.execute(FOREIGN_KEY)
            self.cursor.execute("INSERT INTO Likes(user_id, post_id) VALUES (?,?)", params)
            self.conn.commit()
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(400, "bad request")