from fastapi import FastAPI

from src.auth.router import router as auth_router
from src.config import config

app = FastAPI(
    title=config.APP.TITLE,
    description=config.APP.DESCRIPTION,
    version=config.APP.VERSION,
)


app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the GPA calculator API", "status": "ok"}
