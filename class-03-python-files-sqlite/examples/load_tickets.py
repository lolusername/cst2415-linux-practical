import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CSV_PATH = BASE_DIR / "data" / "tickets.csv"
DB_PATH = BASE_DIR / "tickets.db"

connection = sqlite3.connect(DB_PATH)

connection.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    category TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    created_date TEXT NOT NULL,
    issue TEXT NOT NULL
)
""")

connection.execute("DELETE FROM tickets")

with CSV_PATH.open(newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        connection.execute(
            """
            INSERT INTO tickets (
                id, student_name, category, priority, status, created_date, issue
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                int(row["id"]),
                row["student_name"],
                row["category"],
                row["priority"],
                row["status"],
                row["created_date"],
                row["issue"],
            ),
        )

connection.commit()
connection.close()

print(f"Loaded ticket data into {DB_PATH}")
