from database.db import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) AS total FROM customers")

print(dict(cursor.fetchone()))

conn.close()