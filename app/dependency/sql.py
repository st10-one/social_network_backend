import sqlite3
from typing import Annotated

from os.path import expanduser
from fastapi import Depends

path_home = expanduser("~")

def sql_conn():
    with sqlite3.connect(f"{path_home}/social_network_backend/database/data.db") as conn:
        yield conn


sql_dep = Annotated[sqlite3.Connection, Depends(sql_conn)]
