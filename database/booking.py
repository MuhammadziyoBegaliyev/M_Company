import sqlite3

def get_all_bookings():
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    bookings = cursor.fetchall()
    conn.close()
    return bookings
