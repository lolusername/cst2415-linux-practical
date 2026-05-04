# Lab 01: Terminal Basics And First Python Script

Submit your work in Brightspace if your instructor opens the Lab 01 submission folder.

## Part 1: Create Your Workspace

Run these commands:

```bash
pwd
mkdir -p ~/bootcamp/class01
cd ~/bootcamp/class01
pwd
```

Then answer:

1. What folder are you in after running `cd ~/bootcamp/class01`?
2. What does `mkdir -p` do?

## Part 2: Create And Inspect Files

Run:

```bash
touch notes.txt
ls
ls -la
```

Add text to the file:

```bash
nano notes.txt
```

Type:

```text
Today I used the Linux terminal.
Linux is useful because many servers run it.
```

Save in nano:

- press `Ctrl + O`
- press `Enter`
- press `Ctrl + X`

Inspect the file:

```bash
cat notes.txt
ls -l notes.txt
```

Then answer:

1. What command showed the contents of the file?
2. What command showed permissions?
3. What permissions do you see for `notes.txt`?

## Part 3: Run Python

Check Python:

```bash
python3 --version
```

Create a file:

```bash
nano hello.py
```

Type this code:

```python
print("Hello from Linux")
print("I can run Python from the terminal")
```

Run it:

```bash
python3 hello.py
```

Then answer:

1. What command ran the Python file?
2. What output did you get?

## Part 4: Make A System Info Script

Create:

```bash
nano system_info.py
```

Type:

```python
import os
import platform
import shutil

print("System:", platform.system())
print("Release:", platform.release())
print("Machine:", platform.machine())
print("Python:", platform.python_version())
print("Current folder:", os.getcwd())

total, used, free = shutil.disk_usage(".")
print("Disk total GB:", round(total / (1024 ** 3), 2))
print("Disk free GB:", round(free / (1024 ** 3), 2))
```

Run:

```bash
python3 system_info.py
```

Then answer:

1. What operating system did Python report?
2. What machine type did Python report?
3. Why might a developer need to check this information?

## Part 5: Brightspace Submission

Submit one document, screenshot set, or text file with:

- output from `pwd`
- output from `ls -la`
- output from `python3 --version`
- output from `python3 hello.py`
- output from `python3 system_info.py`
- answers to all written questions

## Reflection

Answer in 3 to 5 sentences:

What did you learn about Linux today, and what still feels confusing?
