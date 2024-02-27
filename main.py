import uvicorn
from fastapi import FastAPI

from user import routers as user_router

app = FastAPI()

app.include_router(user_router.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
