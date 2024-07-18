from fastapi import Depends, HTTPException, status, Cookie
from fastapi.security import OAuth2PasswordBearer
from src.user.schema import LinkedinUser
from jwt import PyJWTError
from .linkedin_oauth import LinkedInOAuth
from src.user.service import UserService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)
credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")


class AuthService:
    def __init__(self):
        self.linkedin_oauth = LinkedInOAuth()

    async def validate_code(self, code: str):
        user_service = UserService()
        user = await self.extract_Linkedin_user_from_callback_code(code)

        if user is None:
            raise credentials_exception

        jwt_token = self.linkedin_oauth.create_access_token(user)

        return await user_service.create_or_update(token=jwt_token, user=user)

    def authenticate_request(
        self, token: str | None = Depends(oauth2_scheme), session: str | None = Cookie(default=None)
    ):
        # Priority: Bearer token > Cookie
        if token is None:
            if session is None:
                raise credentials_exception
            token = session

        try:
            payload = self.linkedin_oauth.decode_access_token(token)
            user_id: str | None = payload.get("sub")

            if user_id is None:
                raise credentials_exception
        except PyJWTError:
            raise credentials_exception

        return payload

    async def extract_Linkedin_user_from_callback_code(self, code: str):
        try:
            token = await self.linkedin_oauth.get_access_token(code)
            user_info = await self.linkedin_oauth.get_user_info(token)
            linkedin_user = LinkedinUser(**user_info)
            return linkedin_user.model_dump()
        except Exception:
            raise credentials_exception
