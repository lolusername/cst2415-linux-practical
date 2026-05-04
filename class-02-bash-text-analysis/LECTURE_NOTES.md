# Lecture Notes: Bash Scripts And Text Analysis

## Big Idea

The Linux command line is powerful because commands can be combined.

One command can list files. Another command can search. Another can count. A pipe lets you connect them.

```mermaid
flowchart LR
    file["tickets.csv"] --> grep["grep password"]
    grep --> cut["cut category column"]
    cut --> sort["sort"]
    sort --> uniq["uniq -c"]
    uniq --> report["quick report"]
```

## Bash

Bash is a shell. It reads commands and can also run command files called scripts.

A simple Bash script starts with a shebang:

```bash
#!/usr/bin/env bash
echo "Hello from Bash"
```

Run it with:

```bash
bash script.sh
```

Or make it executable:

```bash
chmod +x script.sh
./script.sh
```

## Commands For Today

| Command | Use |
| --- | --- |
| `head file` | show first lines |
| `tail file` | show last lines |
| `wc -l file` | count lines |
| `grep "text" file` | search for matching lines |
| `grep -i "text" file` | search case-insensitively |
| `find . -name "*.py"` | find files by name |
| `sort file` | sort lines |
| `uniq -c` | count repeated adjacent lines |
| `cut -d, -f3 file` | split CSV-style text by comma and show field 3 |
| `>` | write output to a file |
| `>>` | append output to a file |
| `|` | pipe output into another command |

## Example Pipeline

Count tickets by category from a CSV file:

```bash
tail -n +2 data/tickets.csv | cut -d, -f3 | sort | uniq -c | sort -nr
```

Meaning:

- skip the header row
- take field 3
- sort matching categories together
- count each category
- sort biggest count first

## Industry Connection

This is basic analysis. Real teams use similar ideas to inspect:

- application logs
- error reports
- server access logs
- CSV exports from systems
- security event text
- test output

The commands are old, but the skill is current: quickly inspect messy data and explain what you found.
