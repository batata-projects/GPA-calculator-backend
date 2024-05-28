from fastapi import FastAPI

app = FastAPI(
    title="GPA Calculator",
    description="A simple GPA calculator API",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Welcome to the GPA calculator API", "status": "ok"}
