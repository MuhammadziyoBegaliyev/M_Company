import sqlite3

def create_promotions_table():
    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS promotions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def create_users_table():
    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            first_name TEXT,
            phone TEXT,
            language TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_promotion(title: str, description: str):
    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO promotions (title, description) VALUES (?, ?)", (title, description))
    conn.commit()
    conn.close()

def get_promotions():
    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description FROM promotions ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_promotion(promo_id: int):
    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM promotions WHERE id = ?", (promo_id,))
    conn.commit()
    conn.close()


def get_all_users():
    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_promotion(promo_id: int):
    conn = sqlite3.connect("booking.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM promotions WHERE id = ?", (promo_id,))
    conn.commit()
    conn.close()
