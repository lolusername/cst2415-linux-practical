import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

DB_PATH = Path("tickets.db")

app = FastAPI(title="Campus Helpdesk Ticket Tracker")


class TicketCreate(BaseModel):
    student_name: str = Field(min_length=1)
    category: str = Field(default="general", min_length=1)
    priority: str = Field(default="normal", min_length=1)
    issue: str = Field(min_length=1)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def row_to_ticket(row):
    return {
        "id": row["id"],
        "student_name": row["student_name"],
        "category": row["category"],
        "priority": row["priority"],
        "status": row["status"],
        "issue": row["issue"],
    }


def init_db():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                category TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                issue TEXT NOT NULL
            )
            """
        )


@app.on_event("startup")
def startup():
    init_db()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tickets")
def list_tickets():
    with get_connection() as connection:
        rows = connection.execute("SELECT * FROM tickets ORDER BY id").fetchall()
    return [row_to_ticket(row) for row in rows]


@app.post("/tickets", status_code=201)
def create_ticket(ticket: TicketCreate):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO tickets (
                student_name, category, priority, status, issue
            ) VALUES (?, ?, ?, ?, ?)
            """,
            (
                ticket.student_name,
                ticket.category,
                ticket.priority,
                "open",
                ticket.issue,
            ),
        )
        connection.commit()
        ticket_id = cursor.lastrowid

        row = connection.execute(
            "SELECT * FROM tickets WHERE id = ?",
            (ticket_id,),
        ).fetchone()

    return row_to_ticket(row)


@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    with get_connection() as connection:
        row = connection.execute(
            "SELECT * FROM tickets WHERE id = ?",
            (ticket_id,),
        ).fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return row_to_ticket(row)
