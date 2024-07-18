from fastapi import APIRouter, Depends
from typing import Annotated
from src.user.service import UserService
from src.auth.service import AuthService


router = APIRouter()
auth_service = AuthService()


@router.get("/me")
async def get_my_user(user: Annotated[dict, Depends(auth_service.authenticate_request)]):
    user_service = UserService()

    return await user_service.get_my_user(user=user)
