# database/contacts.py

import sqlite3

def create_contacts_table():
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            phone TEXT,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def add_contact(user_id, name, phone, message):
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contacts (user_id, name, phone, message)
        VALUES (?, ?, ?, ?)
    """, (user_id, name, phone, message))
    conn.commit()
    conn.close()
