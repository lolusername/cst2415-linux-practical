#!/usr/bin/env bash
set -euo pipefail

DATA_FILE="${1:-data/tickets.csv}"

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
