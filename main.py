from fastapi import FastAPI
from routers import router
from contextlib import asynccontextmanager
from db import create_table, drop_table

import uvicorn

@asynccontextmanager
async def lifespan(app:FastAPI):
   # await drop_table()
    #print("Очищення таблиць")
    await create_table()
    print("Підготовка бази данх")
    yield 


app = FastAPI(lifespan=lifespan, title="Web Social")
app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run("main:app")

