#!/bin/sh
# Optional limited guard; see docs/workflows/GIT.md. Requires Python 3.
if ! command -v python3 >/dev/null 2>&1; then
  echo 'Cofounder guard needs Python 3. Install it or remove this optional hook from Claude settings.' >&2
  exit 2
fi
exec python3 "$(dirname "$0")/cofounder_guard.py"
