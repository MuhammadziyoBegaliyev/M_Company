import aiosqlite

async def create_tables():
    async with aiosqlite.connect("database/bot.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                name TEXT,
                phone TEXT,
                language TEXT
            );
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                category TEXT,
                place_id INTEGER,
                date TEXT,
                status TEXT
            );
        """)
        await db.commit()


async def create_tables():
    async with aiosqlite.connect("database/bot.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                name TEXT,
                phone TEXT,
                language TEXT
            );
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                category TEXT,
                place_id INTEGER,
                date TEXT,
                status TEXT
            );
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                rating INTEGER,
                comment TEXT
            );
        """)
        await db.commit()

async def add_feedback(user_id, rating, comment):
    async with aiosqlite.connect("database/bot.db") as db:
        await db.execute("""
            INSERT INTO feedback (user_id, rating, comment) VALUES (?, ?, ?)
        """, (user_id, rating, comment))
        await db.commit()

async def get_all_feedback():
    async with aiosqlite.connect("database/bot.db") as db:
        async with db.execute("SELECT * FROM feedback") as cursor:
            return await cursor.fetchall()


async def add_user(user_id, name, phone, language):
    async with aiosqlite.connect("database/bot.db") as db:
        await db.execute("""
            INSERT OR REPLACE INTO users (user_id, name, phone, language) VALUES (?, ?, ?, ?)
        """, (user_id, name, phone, language))
        await db.commit()

async def get_user(user_id):
    async with aiosqlite.connect("database/bot.db") as db:
        async with db.execute("""
            SELECT * FROM users WHERE user_id = ?
        """, (user_id,)) as cursor:
            return await cursor.fetchone()

async def update_user_language(user_id, lang):
    async with aiosqlite.connect("database/bot.db") as db:
        await db.execute("""
            UPDATE users SET language = ? WHERE user_id = ?
        """, (lang, user_id))
        await db.commit()


async def get_all_bookings():
    import aiosqlite
    async with aiosqlite.connect("database/bot.db") as db:
        async with db.execute("SELECT * FROM bookings") as cursor:
            return await cursor.fetchall()

async def get_all_users():
    import aiosqlite
    async with aiosqlite.connect("database/bot.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()
        



        ####


    