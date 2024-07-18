import httpx
from src.config import settings
from datetime import datetime, timedelta
import jwt


class LinkedInOAuth:
    def __init__(self):
        self.client_id = settings.LINKEDIN_CLIENT_ID
        self.client_secret = settings.LINKEDIN_CLIENT_SECRET
        self.redirect_uri = settings.LINKEDIN_REDIRECT_URI
        self.base_url = "https://api.linkedin.com/v2"

    def get_authorization_url(self):
        return (
            f"https://www.linkedin.com/oauth/v2/authorization"
            f"?response_type=code&client_id={self.client_id}"
            f"&redirect_uri={self.redirect_uri}"
            f"&scope=profile%20email%20openid"
        )

    async def get_access_token(self, code: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://www.linkedin.com/oauth/v2/accessToken",
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": self.redirect_uri,
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                },
            )
        response.raise_for_status()
        return response.json()["access_token"]

    async def get_user_info(self, access_token: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/userinfo",
                headers={"Authorization": f"Bearer {access_token}"},
            )
        response.raise_for_status()
        return response.json()

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(hours=8)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY)
        return encoded_jwt

    def decode_access_token(self, token: str):
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
