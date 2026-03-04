import sqlite3
from typing import Annotated
from fastapi import Depends, File, Form, UploadFile

from schemas import UsersSchema

def user_data(first_name: str = Form(...), last_name: str = Form(...), username: str = Form(...), bio: str | None = Form(None)) -> UsersSchema:
    return UsersSchema(first_name=first_name, last_name=last_name, username=username, bio=bio)

def sql_conn():
    with sqlite3.connect('/home/stipa/database/data.db') as conn:
        yield conn


sql_dep = Annotated[sqlite3.Connection, Depends(sql_conn)]
file_data = Annotated[UploadFile, File()]
usr_data_dep = Annotated[UsersSchema, Depends(user_data)]
