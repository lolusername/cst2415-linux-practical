import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "tickets.db"

connection = sqlite3.connect(DB_PATH)
connection.row_factory = sqlite3.Row

print("Tickets by category:")
for row in connection.execute("""
    SELECT category, COUNT(*) AS total
    FROM tickets
    GROUP BY category
    ORDER BY total DESC
"""):
    print(f"- {row['category']}: {row['total']}")

print()
print("Open high priority tickets:")
for row in connection.execute("""
    SELECT id, student_name, category, issue
    FROM tickets
    WHERE status = 'open' AND priority = 'high'
    ORDER BY id
"""):
    print(f"- #{row['id']} {row['student_name']} ({row['category']}): {row['issue']}")

connection.close()
