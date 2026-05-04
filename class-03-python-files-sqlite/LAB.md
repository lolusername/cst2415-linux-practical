# Lab 03: Load Tickets Into SQLite

Submit your work in Brightspace if your instructor opens the Lab 03 submission folder.

## Part 1: Set Up

Create a folder:

```bash
mkdir -p ~/bootcamp/class03
cd ~/bootcamp/class03
```

Create or copy `tickets.csv` using the data from this repo's `data/tickets.csv`.

Check Python:

```bash
python3 --version
```

## Part 2: Create The Loader Script

Create:

```bash
nano load_tickets.py
```

Type this code:

```python
import csv
import sqlite3
from pathlib import Path

CSV_PATH = Path("tickets.csv")
DB_PATH = Path("tickets.db")

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
```

Run:

```bash
python3 load_tickets.py
ls -l
```

Then answer:

1. What new file appeared?
2. Why is that file important?

## Part 3: Query The Database With Python

Create:

```bash
nano analyze_tickets.py
```

Type:

```python
import sqlite3

connection = sqlite3.connect("tickets.db")
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
```

Run:

```bash
python3 analyze_tickets.py
```

Then answer:

1. Which category has the most tickets?
2. How many open high priority tickets are listed?
3. What does `WHERE status = 'open' AND priority = 'high'` mean?

## Part 4: Optional SQLite Command Line

If the `sqlite3` command works in your environment, run:

```bash
sqlite3 tickets.db
```

Inside SQLite, run:

```sql
.tables
SELECT COUNT(*) FROM tickets;
SELECT category, COUNT(*) FROM tickets GROUP BY category;
.quit
```

If `sqlite3` is not installed, skip this part and use your Python output.

## Brightspace Submission

Submit:

- output from `python3 --version`
- output from `ls -l` showing `tickets.db`
- your `load_tickets.py`
- your `analyze_tickets.py`
- output from `python3 analyze_tickets.py`
- answers to all written questions

## Reflection

In 4 to 6 sentences, explain the difference between a CSV file and a database. Include one reason a real app would need a database.
