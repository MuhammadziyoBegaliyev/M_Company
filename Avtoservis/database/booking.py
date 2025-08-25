import sqlite3

# 📌 Bazaga ulanish funksiyasi
def get_db():
    conn = sqlite3.connect("booking.db")
    return conn

# 📌 Jadval yaratish
def create_tables():
    conn = get_db()
    cursor = conn.cursor()

    # Servislar jadvali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        photo TEXT
    )
    """)

    conn.commit()
    conn.close()

# 📌 Yangi servis qo‘shish
def add_service(name, description, photo):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO services (name, description, photo) VALUES (?, ?, ?)", (name, description, photo))
    conn.commit()
    conn.close()

# 📌 Servis o‘chirish
def delete_service(service_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM services WHERE id=?", (service_id,))
    conn.commit()
    conn.close()

# 📌 Barcha servislarni olish
def get_all_services():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description, photo FROM services")
    services = cursor.fetchall()
    conn.close()
    return services
