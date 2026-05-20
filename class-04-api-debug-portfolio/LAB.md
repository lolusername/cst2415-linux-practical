# Lab 04: Campus Helpdesk Ticket Tracker API

This is an ungraded in-class skill-building lab. Save your commands, output, screenshots, code, and answers for your own notes.

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

### Fedora Docker CLI Note

You do not need a Linux GUI to run this app. FastAPI runs from the command line.

If you are using a bare Fedora Docker container, Python may not be installed yet. Install the basics first:

```bash
dnf -y install python3 python3-pip curl nano
```

Then continue with the virtual environment commands above.

If you want to open `/docs` in a browser on your host computer while the app runs inside Docker, the container must publish port `8000`, and Uvicorn must listen on `0.0.0.0`.

Example Docker start command from the repo root:

```bash
docker run --rm -it -p 8000:8000 \
  -v "$PWD":/work \
  -w /work/class-04-api-debug-portfolio \
  fedora:rawhide bash
```

Inside the container:

```bash
dnf -y install python3 python3-pip curl nano
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

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

If you are inside Docker and want to open the app from a browser outside the container, run:

```bash
uvicorn main:app --host 0.0.0.0 --reload
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

If you are inside Docker and testing from the host browser, use:

```bash
uvicorn main:app --host 0.0.0.0 --reload
```

Create a ticket, stop the server, restart it, and check that the ticket is still there.

Important: the SQLite version starts with an empty ticket list. If `GET /tickets` returns `[]`, that is not broken. Create a ticket with `POST /tickets`, then check `GET /tickets` again.

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

## Quick Troubleshooting

### `python3: command not found`

Python is not installed in the environment.

On Fedora:

```bash
dnf -y install python3 python3-pip
```

### `curl: command not found`

Install curl:

```bash
dnf -y install curl
```

### Browser Cannot Open `/docs`

If the app is running directly on your machine, open:

```text
http://127.0.0.1:8000/docs
```

If the app is running inside Docker, make sure:

1. the container was started with `-p 8000:8000`
2. Uvicorn was started with `--host 0.0.0.0`

### `GET /tickets` Returns `[]`

This is normal for the SQLite version before any tickets are created. Run `POST /tickets` first.

### Server Says Port 8000 Is Already In Use

Stop the old server with `Ctrl + C`, or use a different port:

```bash
uvicorn main:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001/docs
```

## Practice Evidence

For your own notes, collect:

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
