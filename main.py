from fastapi import FastAPI

from user import routers as user_router

app = FastAPI()

app.include_router(user_router.router)
