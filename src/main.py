from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.common.responses import APIResponse
from src.config import config
from src.controller.status import router as status_router
from src.controller.terms.router import router as terms_router

app = FastAPI(
    title=config.APP.TITLE,
    description=config.APP.DESCRIPTION,
    version=config.APP.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(status_router)
app.include_router(terms_router)


@app.get("/")
async def root():
    return APIResponse(
        message="Welcome to the GPA calculator API", status=status.HTTP_200_OK
    )
