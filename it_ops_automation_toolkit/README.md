# IT Ops & Automation Toolkit

## Overview
A collection of Shell and Python utilities designed to support high‑availability banking environments. These tools automate routine operational checks and provide fast diagnostic insights during incident management.

## Features
### **System Health Check (`health_check.sh`)**
A lightweight Linux-style monitoring script that performs:
- **Process validation** (checks if a critical service is running)
- **Disk usage inspection**
- **Database file presence checks**

This script is intended for Linux environments (Cron, systemd timers, or monitoring agents).  
It can also be executed on Windows via Git Bash or WSL for demonstration purposes.

### **Log Analytics (`log_analyzer.py`)**
A standalone Python utility that:
- Parses large application logs
- Detects key severity levels (`WARN`, `ERROR`, `FATAL`)
- Produces a quick summary of occurrences

Useful for daily log reviews, automated alerting, or integrating into support workflows.

## Senior Support Context
In a fast‑moving environment like **BNP Paribas**, manual monitoring introduces operational risk.  
These tools are designed to reduce MTTR by providing:
- Automated health checks
- Rapid log triage
- Clear, actionable diagnostics

They can be scheduled as **Cron Jobs**, integrated into **Jira Automation**, or used interactively during incident response.

---

## How to Run

### **1. Running the System Health Check**
On Linux or Git Bash:

```bash
bash it_ops_automation_toolkit/scripts/health_check.sh
```

This script runs independently and does **not** call the Python log analyzer.

---

### **2. Running the Log Analyzer**
From the project root:

```bash
python it_ops_automation_toolkit/scripts/log_analyzer.py it_ops_automation_toolkit/data/app.log
```

Or using module syntax:

```bash
python -m it_ops_automation_toolkit.scripts.log_analyzer it_ops_automation_toolkit/data/app.log
```

This produces output like:

```
--- Daily Log Summary ---
WARN: 1 occurrences
ERROR: 2 occurrences
FATAL: 1 occurrences
```

---

## Project Structure

```
it_ops_automation_toolkit/
│
├── scripts/
│   ├── health_check.sh
│   └── log_analyzer.py
│
└── data/
    └── app.log
```

Each tool is intentionally independent so they can be used flexibly in different operational contexts.
