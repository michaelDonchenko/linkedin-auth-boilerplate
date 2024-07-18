from sqlalchemy import Column, Integer, String, DateTime
from src.database import BaseSQLModel
from sqlalchemy.sql import func


class User(BaseSQLModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True)
    picture = Column(String, nullable=True)
    created = Column(DateTime, default=func.now())
    last_active = Column(DateTime, insert_default=func.now())

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"
