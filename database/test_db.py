import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM customers")
print(cursor.fetchall())

cursor.execute("SELECT * FROM products")
print(cursor.fetchall())

cursor.execute("SELECT * FROM orders LIMIT 5")
print(cursor.fetchall())

conn.close()