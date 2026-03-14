from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine("/home/stipa/database/data.db")
async_session = async_sessionmaker(bind=engine)

async def sessions():
    async with async_session as asy_session:
        yield asy_session


async def create_table():
    async with engine.begin() as conn:
        conn.run_sync()