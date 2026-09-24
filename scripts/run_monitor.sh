#!/usr/bin/env bash

set -u

# Find the project root regardless of where this script is called from.
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT" || exit 1

# Use a virtual environment if available.
if [[ -x "$PROJECT_ROOT/venv/bin/python" ]]; then
    PYTHON="$PROJECT_ROOT/venv/bin/python"
elif [[ -x "$PROJECT_ROOT/.venv/bin/python" ]]; then
    PYTHON="$PROJECT_ROOT/.venv/bin/python"
else
    PYTHON="python3"
fi

# Create reports directory if it does not exist.
REPORT_DIR="${REPORT_DIR:-$PROJECT_ROOT/reports}"
mkdir -p "$REPORT_DIR"

# Create a timestamped automation log.
TIMESTAMP="$(date '+%Y%m%d_%H%M%S')"
RUN_LOG="$REPORT_DIR/automation_$TIMESTAMP.log"

echo "========================================"
echo " Linux System Monitor - Bash Automation"
echo "========================================"
echo "Project: $PROJECT_ROOT"
echo "Python:  $PYTHON"
echo "Started: $(date)"
echo

# Run the Python application as a module so that
# imports such as "from src.config import get_config" work correctly.
# tee displays the output and also saves it to the log file.
set +e
"$PYTHON" -m src.main "$@" 2>&1 | tee "$RUN_LOG"
PYTHON_STATUS=${PIPESTATUS[0]}
set -e

echo
echo "Finished: $(date)"
echo "Run log:  $RUN_LOG"
echo "Exit code: $PYTHON_STATUS"

# Return the same exit code as the Python application.
exit "$PYTHON_STATUS"
