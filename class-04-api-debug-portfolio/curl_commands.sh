#!/usr/bin/env bash
set -euo pipefail

curl http://127.0.0.1:8000/health
echo

curl http://127.0.0.1:8000/tickets
echo

curl -X POST http://127.0.0.1:8000/tickets \
  -H "Content-Type: application/json" \
  -d '{"student_name":"Blake","category":"software","priority":"normal","issue":"Python package install question"}'
echo
