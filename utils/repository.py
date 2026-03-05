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
    def update_user():
        raise NotImplemented
    
    def delete_user():
        raise NotImplemented

    @abstractmethod
    def add_posts():
        raise NotImplemented

    @abstractmethod
    def add_like():
        raise NotImplemented


#---------------------------------------- make class Repository ----------------------------------------#

class SQLRepository(AbstractRepository):
    def __init__(self): # initialization 
        self.conn = sqlite3.connect('/home/stipa/database/data.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

                                        
#---------------------------------------- Users ----------------------------------------#

    def add_user(self, data: UsersModel, content) -> UsersModel:  #add new user in database
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

        return {
            "first_name": data.first_name,
            "last_name": data.last_name,
            "username": data.username,
            "bio": data.bio
        }

    def get_user_name(self, name: str): #get one user
        try:
            self.cursor.execute("SELECT first_name, last_name, username FROM Users Where username = ? or first_name = ?", (name, name,))
            result = self.cursor.fetchone()
        except sqlite3.Error, TypeError:
            raise HTTPException(404, "not found")
        
        return {
            "data": result
        }
        
    def update_user(self, user_id: int, data: UsersModel) -> UsersModel: #update data user profil
        params = (
            data.first_name, data.last_name,
            data.username, data.bio,
            user_id
        )

        try:
            self.cursor.execute("UPDATE Users SET first_name = ?, last_name = ?, username = ?, bio = ? Where id = ?", params)
            self.conn.commit()
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(400, "bad request")
        
        return {
            "user_id": user_id,
            "first_name": data.first_name,
            "last_name": data.last_name,
            "username": data.username,
            "bio": data.bio
        }
        
    def delete_user(self, user_id:int):
        try:
            self.cursor.execute("DELETE FROM Users Where id = ?", (user_id,))
            self.conn.commit()
        except sqlite3.Error:
            self.conn.rollback()
            raise HTTPException(400, "bad request")
            
        return {"user_id": user_id}
        
 #---------------------------------------- Posts ----------------------------------------#  

    def add_posts(self, data: PostModel):
        params = (
            data.user_id, data.content
        )

        try:
            self.cursor.execute(FOREIGN_KEY)
            self.cursor.execute("INSERT INTO Posts(user_id, content) VALUES (?,?)", params)
            self.conn.commit()
            return {"id": data.user_id, "content": data.content}
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(400, "bad request")
        

#---------------------------------------- Likes ----------------------------------------#

    def add_like(self, data:LikesModel):
        params = (
            data.user_id, data.post_id
        )

        try:
            self.cursor.execute(FOREIGN_KEY)
            self.cursor.execute("INSERT INTO Likes(user_id, post_id) VALUES (?,?)", params)
            self.conn.commit()
            return params
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(400, "bad request")