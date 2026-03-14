import sqlite3
from typing import Annotated

from fastapi import Depends


def sql_conn():
    with sqlite3.connect("/home/stipa/database/data.db") as conn:
        yield conn


sql_dep = Annotated[sqlite3.Connection, Depends(sql_conn)]
