from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from contextlib import asynccontextmanager

connection_string = "postgresql+asyncpg://postgres:password@localhost:5432/fastapi-linkedin-auth"


class BaseSQLModel(DeclarativeBase):
    pass


engine = create_async_engine(
    connection_string,
    echo=True,
    future=True,
)


def async_session_generator():
    return async_sessionmaker(engine, class_=AsyncSession)


@asynccontextmanager
async def get_session():
    try:
        async_session = async_session_generator()

        async with async_session() as session:
            yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
