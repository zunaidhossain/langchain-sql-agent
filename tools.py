import re
import sqlite3
from typing import Any

from langchain_core.tools import tool

from database.db import get_connection


@tool
def execute_sql(query: str) -> list[dict[str, Any]]:
    """
    Execute a read-only SQLite SELECT query.

    Use this tool whenever information needs to be retrieved
    from the database.
    """

    query = query.strip().rstrip(";")

    # Only allow SELECT queries
    if not re.match(r"^SELECT\b", query, re.IGNORECASE):
        raise ValueError(
            "Only SELECT queries are allowed."
        )

    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        return [dict(row) for row in rows]

    except sqlite3.Error as e:
        return [
            {
                "error": str(e)
            }
        ]

    finally:
        conn.close()