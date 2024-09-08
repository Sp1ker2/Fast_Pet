
import uvicorn
from fastapi import FastAPI, Depends

from database import create_tables, delete_tables
from contextlib import asynccontextmanager
from router import router as task_router
tasks = []
@asynccontextmanager
async def lifespan(app:FastAPI):
    # await delete_tables()
    # print("clear")
    await create_tables()
    print("on")
    yield
    print("Off")
app = FastAPI(lifespan=lifespan)


app.include_router(task_router,tags=['tasks'])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)