#!/bin/bash

# Configuration
APP_NAME="RiskEngine"
LOG_FILE="/var/log/app_monitor.log"
THRESHOLD=90

echo "--- Starting System Health Check ---"

# 1. Check if a process is running (e.g., the Java app)
if pgrep -x "$APP_NAME" > /dev/null
then
    echo "[OK] $APP_NAME is running."
else
    echo "[ALERT] $APP_NAME is NOT running!"
fi

# 2. Check Disk Usage
DISK_USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')
if [ "$DISK_USAGE" -gt "$THRESHOLD" ]; then
    echo "[WARNING] Disk usage is above $THRESHOLD% (Current: $DISK_USAGE%)"
else
    echo "[OK] Disk usage is at $DISK_USAGE%."
fi

# 3. Check DB Connectivity (Mock check for SQLite)
if [ -f "./banking_risk.db" ]; then
    echo "[OK] Database file detected."
else
    echo "[CRITICAL] Database file missing!"
fi