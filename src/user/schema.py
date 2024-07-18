from pydantic import BaseModel
from typing import Optional


class Locale(BaseModel):
    country: str
    language: str


class LinkedinUser(BaseModel):
    sub: str
    email_verified: bool
    name: str
    locale: Optional[Locale]
    given_name: Optional[str]
    family_name: Optional[str]
    email: Optional[str]
    picture: Optional[str]
