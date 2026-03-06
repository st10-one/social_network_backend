from fastapi import FastAPI
from routers import users, likes, posts
from contextlib import asynccontextmanager
from db import create_table, drop_table

import uvicorn

@asynccontextmanager
async def lifespan(app:FastAPI):
    await drop_table()
    print("clean table")
    await create_table()
    print("Database is ready for work!")
    yield 


app = FastAPI(lifespan=lifespan, title="Web Social")


app.include_router(users.router)
app.include_router(posts.router)
app.include_router(likes.router)

@app.get("/", tags=["root"])
def root():
    return "Hello!"

if __name__ == "__main__":
    uvicorn.run("main:app")

