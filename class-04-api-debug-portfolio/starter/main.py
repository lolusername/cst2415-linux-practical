from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Campus Helpdesk Ticket Tracker")


class TicketCreate(BaseModel):
    student_name: str = Field(min_length=1)
    category: str = Field(default="general", min_length=1)
    priority: str = Field(default="normal", min_length=1)
    issue: str = Field(min_length=1)


tickets = [
    {
        "id": 1,
        "student_name": "Ari",
        "category": "password",
        "priority": "normal",
        "status": "open",
        "issue": "password reset needed",
    }
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tickets")
def list_tickets():
    return tickets


@app.post("/tickets", status_code=201)
def create_ticket(ticket: TicketCreate):
    new_ticket = ticket.dict()
    new_ticket["id"] = len(tickets) + 1
    new_ticket["status"] = "open"
    tickets.append(new_ticket)
    return new_ticket


@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    raise HTTPException(status_code=404, detail="Ticket not found")
