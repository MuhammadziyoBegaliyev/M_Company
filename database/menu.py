import sqlite3

def create_menu_table():
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            name TEXT,
            description TEXT,
            price REAL
        )
    """)
    conn.commit()
    conn.close()

def add_menu_item(category, name, description, price):
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO menu (category, name, description, price) VALUES (?, ?, ?, ?)",
        (category, name, description, price)
    )
    conn.commit()
    conn.close()

def get_menu_items():
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, category, name, description, price FROM menu")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_menu_item(item_id):
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM menu WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
