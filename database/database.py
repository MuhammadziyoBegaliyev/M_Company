import sqlite3


def get_all_bookings():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone, date, cottage FROM bookings")
    rows = cursor.fetchall()
    conn.close()

    results = []
    for row in rows:
        results.append({
            "name": row[0],
            "phone": row[1],
            "date": row[2],
            "cottage": row[3]
        })
    return results
