from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).resolve().parent / "shop.db"


def create_tables():
    conn = sqlite3.connect(DB_PATH)

    conn.execute("PRAGMA foreign_keys = ON")

    cursor = conn.cursor()

    # -----------------------------
    # Customers Table
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            city TEXT NOT NULL
        );
    """)

    # -----------------------------
    # Products Table
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        );
    """)

    # -----------------------------
    # Orders Table
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT NOT NULL
                CHECK(status IN ('Pending', 'Delivered', 'Cancelled')),
            order_date TEXT NOT NULL,
            FOREIGN KEY(customer_id)
                REFERENCES customers(id),
            FOREIGN KEY(product_id)
                REFERENCES products(id)
        );
    """)

    conn.commit()
    conn.close()

    print("Database created successfully.")
    print(f"Location: {DB_PATH}")


if __name__ == "__main__":
    create_tables()