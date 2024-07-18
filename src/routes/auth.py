from fastapi import APIRouter
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.responses import RedirectResponse
from src.auth.linkedin_oauth import LinkedInOAuth
from src.auth.service import AuthService


router = APIRouter()
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://www.linkedin.com/oauth/v2/authorization",
    tokenUrl="https://www.linkedin.com/oauth/v2/accessToken",
)


@router.get("/login/linkedin")
async def login_linkedin() -> RedirectResponse:
    linkedin_oauth = LinkedInOAuth()
    authorization_url: str = linkedin_oauth.get_authorization_url()
    return RedirectResponse(url=authorization_url, status_code=307)


@router.get("/callback/linkedin")
async def callback_linkedin(code: str):
    auth_service = AuthService()
    return await auth_service.validate_code(code)
