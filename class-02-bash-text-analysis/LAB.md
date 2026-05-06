# Lab 02: Bash Ticket Report

This is an ungraded in-class skill-building lab. Save your commands, output, screenshots, script, and answers for your own notes.

## Part 1: Set Up

Create your class folder:

```bash
mkdir -p ~/bootcamp/class02
cd ~/bootcamp/class02
```

Create a file named `tickets.csv` and copy the data from this repo's `data/tickets.csv`.

If you cloned this repo, you can also run the lab from this folder:

```bash
cd class-02-bash-text-analysis
```

## Part 2: Inspect The Data

Run:

```bash
head tickets.csv
wc -l tickets.csv
```

Then answer:

1. What does `head` show?
2. How many lines are in the file?
3. Why is the number of data records one less than the line count?

## Part 3: Search With Grep

Run:

```bash
grep "network" tickets.csv
grep -i "password" tickets.csv
grep ",high," tickets.csv
```

Then answer:

1. What does `grep` do?
2. What does `grep -i` change?
3. How many high priority tickets did you find?

## Part 4: Build A Pipeline

Run:

```bash
tail -n +2 tickets.csv | cut -d, -f3
tail -n +2 tickets.csv | cut -d, -f3 | sort
tail -n +2 tickets.csv | cut -d, -f3 | sort | uniq -c
tail -n +2 tickets.csv | cut -d, -f3 | sort | uniq -c | sort -nr
```

Then answer:

1. What does the pipe symbol `|` do?
2. What column are you counting?
3. Which category appears most often?

## Part 5: Write A Bash Script

Create:

```bash
nano ticket_report.sh
```

Type:

```bash
#!/usr/bin/env bash
set -euo pipefail

DATA_FILE="${1:-tickets.csv}"

echo "Ticket file: $DATA_FILE"
echo

echo "Total ticket records:"
tail -n +2 "$DATA_FILE" | wc -l
echo

echo "Tickets by category:"
tail -n +2 "$DATA_FILE" | cut -d, -f3 | sort | uniq -c | sort -nr
echo

echo "High priority tickets:"
grep ",high," "$DATA_FILE" || true
```

Run it:

```bash
bash ticket_report.sh
```

Make it executable:

```bash
chmod +x ticket_report.sh
./ticket_report.sh
```

Save the output:

```bash
./ticket_report.sh > report.txt
cat report.txt
```

## Part 6: Find Files

Run:

```bash
find . -name "*.sh"
find . -name "*.txt"
```

Then answer:

1. What did `find` locate?
2. Why is `find` useful on a Linux system?

## Practice Evidence

For your own notes, collect:

- output from `head tickets.csv`
- output from the category-count pipeline
- your `ticket_report.sh` script
- output from `cat report.txt`
- answers to all written questions

## Reflection

In 4 to 6 sentences, explain how Bash scripts and pipelines could help someone working in IT support, QA testing, cybersecurity, or software development.
