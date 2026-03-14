import sqlite3
from fastapi import HTTPException


from db import UsersModel
from .parents_class import AbstractUserRepository
from .conf import FOREIGN_KEY, PATH_HOME


class UserRepository(AbstractUserRepository):
    def __init__(self):
        self.conn = sqlite3.connect(
            f"{PATH_HOME}/vs_code/social_network_backend/database/data.db", check_same_thread=False
        )
        self.cursor = self.conn.cursor()
    
    def add_user(
        self, data: UsersModel
    ) -> UsersModel:  # add new user in database
        params = (data.first_name, data.last_name, data.username, data.bio)

        try:
            self.cursor.execute(
                "INSERT INTO Users(first_name, last_name, username, bio) VALUES (?,?,?,?)",
                params,
            )
            self.conn.commit()
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(status_code=400, detail=f"user with this name exist\n")

        return {
            "first_name": data.first_name,
            "last_name": data.last_name,
            "username": data.username,
            "bio": data.bio,
        }

    def get_user_name(self, name: str):  # get one user
        pattern = f"{name}%"

        try:
            self.cursor.execute(
                "SELECT first_name, last_name, username FROM Users Where username LIKE ? or first_name LIKE ?",
                (
                    pattern,
                    pattern,
                ),
            )
            result = self.cursor.fetchone()
        except sqlite3.Error, TypeError:
            raise HTTPException(404, "not found")

        return {"data": result}

    def update_user(
        self, user_id: int, data: UsersModel
    ) -> UsersModel:  # update data user profil
        params = (data.first_name, data.last_name, data.username, data.bio, user_id)

        try:
            self.cursor.execute(
                "UPDATE Users SET first_name = ?, last_name = ?, username = ?, bio = ? Where id = ?",
                params,
            )
            self.conn.commit()
        except sqlite3.Error, TypeError:
            self.conn.rollback()
            raise HTTPException(400, "bad request")

        return {
            "user_id": user_id,
            "first_name": data.first_name,
            "last_name": data.last_name,
            "username": data.username,
            "bio": data.bio,
        }

    def delete_user(self, user_id: int):
        try:
            self.cursor.execute(FOREIGN_KEY)
            self.cursor.execute("DELETE FROM Users Where id = ?", (user_id,))
            self.conn.commit()
        except sqlite3.Error:
            self.conn.rollback()
            raise HTTPException(400, "bad request")

        return {"user_id": user_id}