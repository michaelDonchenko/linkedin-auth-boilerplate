from fastapi import FastAPI
from src.routes import auth, user


app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/users", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI LinkedIn OAuth boilerplate"}
