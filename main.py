from fastapi import FastAPI

from database.db import engine, Base
from routers import user as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router.router, prefix="/user")
