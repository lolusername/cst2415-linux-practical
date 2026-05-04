# Lab 04: Campus Helpdesk Ticket Tracker API

Submit your work in Brightspace if your instructor opens the Lab 04 submission folder.

## Part 1: Set Up

Create a folder:

```bash
mkdir -p ~/bootcamp/class04
cd ~/bootcamp/class04
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install packages:

```bash
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn
```

If installation fails, skip to Part 7.

## Part 2: Create The App

Create:

```bash
nano main.py
```

Type the starter version from `starter/main.py`.

Run:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Part 3: Test The API

In the `/docs` page:

1. run `GET /health`
2. run `GET /tickets`
3. run `POST /tickets`
4. run `GET /tickets/{ticket_id}`

Example ticket JSON:

```json
{
  "student_name": "Ari",
  "category": "network",
  "priority": "high",
  "issue": "wifi drops during class"
}
```

## Part 4: Use Curl From The Terminal

Open another terminal in the same folder and run:

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/tickets
```

Create a ticket:

```bash
curl -X POST http://127.0.0.1:8000/tickets \
  -H "Content-Type: application/json" \
  -d '{"student_name":"Blake","category":"software","priority":"normal","issue":"Python package install question"}'
```

## Part 5: Add SQLite Persistence

Replace your `main.py` with the SQLite version from `final/main.py`, or update your file section by section with your instructor.

Stop the server with `Ctrl + C`, then restart:

```bash
uvicorn main:app --reload
```

Create a ticket, stop the server, restart it, and check that the ticket is still there.

Then answer:

1. What file stores the database?
2. How do you know the ticket persisted after restart?
3. Why is persistence important for real apps?

## Part 6: Debugging Practice

Try one safe mistake:

1. Temporarily misspell `FastAPI` as `FastAPi`.
2. Restart the server.
3. Read the error.
4. Fix the typo.

Then answer:

1. What error did you see?
2. What file did the error point to?
3. How did you fix it?

## Part 7: Written Analysis Option

Use this if installs are blocked.

Read `starter/main.py` and `final/main.py`, watch the instructor demo, then answer:

1. What does `GET /health` prove?
2. What does `POST /tickets` do?
3. What is SQLite used for?
4. What is one error that could happen when starting the app?
5. How would you explain this project to an employer in 3 sentences?

## Brightspace Submission

Submit:

- screenshot or copied output of `/docs`
- output from `GET /health`
- one successful `POST /tickets` request and response
- output from `GET /tickets`
- evidence that SQLite persistence worked, or the written analysis option
- your final `main.py`
- short project explanation

## Reflection

Write 5 to 8 sentences:

Explain how Linux, Python, FastAPI, and SQLite worked together in this project. Include one job role where these skills could be useful.
