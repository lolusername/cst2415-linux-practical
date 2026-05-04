# Lecture Notes: Python Files And SQLite

## Big Idea

In Class 02, you used Bash to inspect text. In Class 03, you use Python to make the work more structured and repeatable.

```mermaid
flowchart LR
    csv["CSV file"] --> python["Python script"]
    python --> sqlite["SQLite database file"]
    sqlite --> queries["queries and reports"]
```

## Data Storage Options

| Storage | Good For | Limitation |
| --- | --- | --- |
| Memory list | quick experiments | disappears when program stops |
| Text or CSV file | simple sharing | harder to query safely |
| SQLite | small real apps and labs | not designed for many servers writing at once |
| PostgreSQL or MySQL | production systems | requires server setup |

## CSV

CSV means comma-separated values.

Example:

```text
id,student_name,category,priority,status
1,Ari,password,normal,open
```

Python can read CSV files with the built-in `csv` module.

## SQLite

SQLite stores tables inside a local database file.

Important words:

- table: collection of related rows
- row: one record
- column: one field in a record
- primary key: unique ID for a row
- query: request for data

## SQL Examples

Create a table:

```sql
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    category TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    created_date TEXT NOT NULL,
    issue TEXT NOT NULL
);
```

Count tickets by category:

```sql
SELECT category, COUNT(*) AS total
FROM tickets
GROUP BY category
ORDER BY total DESC;
```

## Industry Connection

Almost every useful application stores data. Even AI tools, dashboards, helpdesk tools, QA systems, and websites need a way to save and retrieve information.

SQLite is a good first database because you can focus on the idea of tables and queries without managing a separate server.
