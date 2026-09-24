#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV="$PROJECT_DIR/.venv"
REPORT_FILE="${REPORT_FILE:-$PROJECT_DIR/reports/system_report.txt}"
LOG_FILE="${MONITOR_LOG_FILE:-$PROJECT_DIR/logs/system.log}"

# Check virtual environment
if [ ! -d "$VENV" ]; then
    echo "Error: Virtual environment not found."
    exit 1
fi

# Activate virtual environment
source "$VENV/bin/activate"

# Move to project directory
cd "$PROJECT_DIR" || exit 1

echo "Linux System Monitor"
echo "===================="
echo

# Run Python monitoring application
python -m src.main "$LOG_FILE"
STATUS=$?

# Check Python program status
if [ "$STATUS" -ne 0 ]; then
    echo
    echo "Monitor failed with exit status $STATUS."
    exit "$STATUS"
fi

echo
echo "Report:"
echo "-------"

# Display generated report
if [ -f "$REPORT_FILE" ]; then
    cat "$REPORT_FILE"
else
    echo "Error: Report file was not created."
    exit 1
fi

exit 0