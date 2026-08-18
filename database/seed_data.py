from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).resolve().parent / "shop.db"


def seed_database():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    # ---------------------------------
    # Clear existing data (optional)
    # ---------------------------------
    cursor.execute("DELETE FROM orders")
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM customers")

    # Reset AUTOINCREMENT counters
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='orders'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='products'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='customers'")

    # ---------------------------------
    # Customers
    # ---------------------------------

    customers = [
        ("Alice Johnson", "alice@gmail.com", "Delhi"),
        ("Bob Smith", "bob@gmail.com", "Mumbai"),
        ("Charlie Brown", "charlie@gmail.com", "Delhi"),
        ("David Wilson", "david@gmail.com", "Kolkata"),
        ("Eva Thomas", "eva@gmail.com", "Bengaluru"),
        ("Frank Miller", "frank@gmail.com", "Hyderabad"),
        ("Grace Lee", "grace@gmail.com", "Chennai"),
        ("Henry Adams", "henry@gmail.com", "Pune"),
        ("Isabella King", "isabella@gmail.com", "Delhi"),
        ("Jack White", "jack@gmail.com", "Mumbai")
    ]

    cursor.executemany(
        """
        INSERT INTO customers(name,email,city)
        VALUES(?,?,?)
        """,
        customers
    )

    # ---------------------------------
    # Products
    # ---------------------------------

    products = [
        ("Laptop", "Electronics", 65000, 8),
        ("Smartphone", "Electronics", 35000, 15),
        ("Headphones", "Electronics", 2500, 40),
        ("Keyboard", "Accessories", 1800, 30),
        ("Mouse", "Accessories", 900, 45),
        ("Monitor", "Electronics", 12000, 10),
        ("Office Chair", "Furniture", 8500, 12),
        ("Desk Lamp", "Furniture", 1500, 22),
        ("Tablet", "Electronics", 22000, 9),
        ("USB-C Cable", "Accessories", 500, 60)
    ]

    cursor.executemany(
        """
        INSERT INTO products(name,category,price,stock)
        VALUES(?,?,?,?)
        """,
        products
    )

    # ---------------------------------
    # Orders
    # customer_id, product_id already exist
    # ---------------------------------

    orders = [
        (1, 1, 1, "Delivered", "2026-07-01"),
        (2, 2, 2, "Pending", "2026-07-02"),
        (3, 3, 3, "Delivered", "2026-07-03"),
        (4, 4, 4, "Cancelled", "2026-07-04"),
        (5, 5, 5, "Delivered", "2026-07-05"),
        (6, 6, 6, "Pending", "2026-07-06"),
        (7, 7, 7, "Delivered", "2026-07-07"),
        (8, 8, 8, "Pending", "2026-07-08"),
        (9, 9, 9, "Delivered", "2026-07-09"),
        (10, 10, 10, "Delivered", "2026-07-10"),

        (1, 3, 2, "Pending", "2026-07-11"),
        (2, 5, 3, "Delivered", "2026-07-12"),
        (3, 6, 1, "Delivered", "2026-07-13"),
        (4, 1, 1, "Pending", "2026-07-14"),
        (5, 10, 6, "Delivered", "2026-07-15"),
        (6, 2, 1, "Delivered", "2026-07-16"),
        (7, 3, 5, "Delivered", "2026-07-17"),
        (8, 9, 1, "Cancelled", "2026-07-18"),
        (9, 4, 2, "Delivered", "2026-07-19"),
        (10, 8, 4, "Pending", "2026-07-20"),

        (1, 6, 1, "Delivered", "2026-07-21"),
        (2, 7, 1, "Delivered", "2026-07-22"),
        (3, 2, 2, "Pending", "2026-07-23"),
        (5, 1, 1, "Delivered", "2026-07-24"),
        (9, 3, 4, "Delivered", "2026-07-25"),
        (4, 9, 1, "Delivered", "2026-07-26"),
        (8, 5, 2, "Pending", "2026-07-27"),
        (6, 10, 10, "Delivered", "2026-07-28"),
        (7, 4, 3, "Delivered", "2026-07-29"),
        (10, 1, 1, "Cancelled", "2026-07-30")
    ]

    cursor.executemany(
        """
        INSERT INTO orders(
            customer_id,
            product_id,
            quantity,
            status,
            order_date
        )
        VALUES(?,?,?,?,?)
        """,
        orders
    )

    conn.commit()
    conn.close()

    print("Database seeded successfully.")


if __name__ == "__main__":
    seed_database()