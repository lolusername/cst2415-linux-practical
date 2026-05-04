# Campus Helpdesk Ticket Tracker

## What I Built

I built a small backend API for helpdesk tickets.

## Tools Used

- Linux terminal
- Python
- FastAPI
- SQLite
- curl or browser API docs

## What The App Can Do

- check app health with `GET /health`
- list tickets with `GET /tickets`
- create tickets with `POST /tickets`
- view one ticket with `GET /tickets/{ticket_id}`
- store tickets in SQLite

## How To Run

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install fastapi uvicorn
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## What I Learned

Write 4 to 6 sentences about what Linux, Python, FastAPI, and SQLite did in this project.
