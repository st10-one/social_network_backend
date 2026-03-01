import sqlite3
from fastapi import Form

from .schemas import UsersSchema

def user_data(first_name: str = Form(...), last_name: str = Form(...), username: str = Form(...), bio: str | None = Form(None)) -> UsersSchema:
    return UsersSchema(first_name=first_name, last_name=last_name, username=username, bio=bio)

def sql_conn():
    with sqlite3.connect('/home/stipa/database/data.db') as conn:
        yield conn