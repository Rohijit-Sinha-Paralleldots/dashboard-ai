from sqlalchemy.ext.asyncio import AsyncSession
from .database import async_session_maker, engine


async def get_db_session():
    db: AsyncSession = async_session_maker()
    try:
        yield db
    finally:
        await db.close()


async def get_db_engine():
    conn = await engine.connect()
    try:
        yield conn
    finally:
        await conn.close()
