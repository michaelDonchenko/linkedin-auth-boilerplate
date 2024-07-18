from typing import Any
from .models import User
from src.database import get_session
from sqlalchemy import insert, select


class UserService:
    async def get_my_user(self, user: dict):
        async with get_session() as session:
            result = await session.execute(select(User).where(User.email == user["email"]))
            myUser = result.scalars().first()
            return {"user": myUser}

    async def create_or_update(self, token: str, user: dict[str, Any]):
        async with get_session() as session:
            if "email" in user:
                result = await session.execute(select(User).where(User.email == user["email"]))
                found_user = result.scalars().first()

                if found_user:
                    return {"token": token, "user": found_user}
                else:
                    insert_stmt = insert(User).values(name=user["name"], email=user["email"], picture=user["picture"])
                    result = await session.execute(insert_stmt)
                    await session.commit()

                    if result.inserted_primary_key:
                        new_user_id = result.inserted_primary_key[0]

                    new_user = await session.get(User, new_user_id)

                    return {"token": token, "user": new_user}
