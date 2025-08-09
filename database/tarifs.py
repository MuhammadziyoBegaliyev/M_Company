
import sqlite3

def create_tarifs_table():
    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarifs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL
    )
    """)
    conn.commit()
    conn.close()

def add_tarif(name, description, price):
    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarifs (name, description, price) VALUES (?, ?, ?)", (name, description, price))
    conn.commit()
    conn.close()

def get_tarifs():
    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarifs")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_tarif(tarif_id):
    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarifs WHERE id = ?", (tarif_id,))
    conn.commit()
    conn.close()