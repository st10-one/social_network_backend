import aiosqlite

async def create_table():
    """
    Ми тут створюємо таблицю в базу даних
    """
    async with aiosqlite.connect('/home/stipa/database/data.db', check_same_thread=False) as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS Users(
	        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	        first_name TEXT not NULL,
	        last_name TEXT,
	        username TEXT UNIQUE NOT NULL,
	        bio TEXT(1000) DEFAULT NULL,
            photo_profil BLOB NOT NULL,
            create_at time DEFAULT CURRENT_TIMESTAMP
    )""")

        await conn.execute("CREATE TABLE IF NOT EXISTS Posts(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, content TEXT, create_at time DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE)")
        await conn.execute("CREATE TABLE IF NOT EXISTS Likes(user_id integer, post_id integer, create_at time DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE FOREIGN KEY (post_id) REFERENCES Posts(id) ON DELETE CASCADE)")

    

async def drop_table():
    async with aiosqlite.connect('/home/stipa/database/data.db', check_same_thread=False) as conn:
        await conn.execute("DROP TABLE IF EXISTS Users")
        await conn.execute("DROP TABLE IF EXISTS Posts")
        await conn.execute("DROP TABLE IF EXISTS likes")
