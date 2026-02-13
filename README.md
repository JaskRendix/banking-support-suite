# **Application Support Portfolio — Full‑Stack Banking Operations**

This repository brings together four complementary projects that demonstrate the technical breadth, analytical mindset, and operational discipline expected from a senior Application Support professional in a banking environment.

It showcases end‑to‑end capabilities across **ETL pipelines**, **operational tooling**, **backend diagnostics**, and **frontend support interfaces** — the core pillars of modern support for risk and finance applications.

---

# Repository Structure

```
/
├── banking_data_pipeline_python/     # Credit Risk ETL (Python)
├── it_ops_automation_toolkit/        # Shell + Python Ops Tools
├── support-portal-backend/           # Spring Boot Support API
└── support-portal-frontend/          # Angular Support Portal UI
```

Each module is self‑contained and can run independently.

---

# Project Overview

## **1. Credit Risk ETL Pipeline (Python)**  
A production‑style ETL that computes **Risk‑Weighted Assets (RWA)** using standard credit‑risk parameters (EAD, PD, LGD).  
Includes data‑quality checks, logging, error handling, and SQLite output.

**Run:**
```bash
pip install -e banking_data_pipeline_python
python -m banking_data_pipeline.rwa_calculator
```

---

## **2. IT Ops & Automation Toolkit**  
A set of lightweight tools used for daily operational checks and incident triage.

- `health_check.sh` — process, disk, and file monitoring  
- `log_analyzer.py` — parses logs and summarizes WARN/ERROR/FATAL  

These scripts reflect real support workflows: control points, monitoring, and rapid diagnostics.

---

## **3. Support Portal Backend (Spring Boot, Java 17)**  
A REST API exposing transaction data and surfacing failures with clear error codes.  
Includes health checks, filtering endpoints, and an H2 in‑memory database for fast prototyping.

**Run:**
```bash
mvn clean spring-boot:run
```

---

## **4. Support Portal Frontend (Angular)**  
A simple UI for viewing system health and failed transactions.  
Designed to give support teams quick visibility into issues.

**Run:**
```bash
ng serve
```

---

# End‑to‑End Flow

The four modules together simulate a realistic support ecosystem:

1. **ETL pipeline** processes credit‑risk data.  
2. **Ops toolkit** monitors the environment and analyzes logs.  
3. **Backend API** exposes diagnostic information.  
4. **Frontend UI** presents it clearly for support teams.

This mirrors the lifecycle of supporting a banking application:  
**data → monitoring → diagnostics → user visibility**.

---

# Skills Demonstrated

- Python (ETL, data quality, logging)  
- SQL (SQLite, H2)  
- Java (Spring Boot)  
- Angular (TypeScript)  
- UNIX Shell scripting  
- Operational monitoring & log analysis  
- Credit‑risk concepts (RWA, PD, LGD, EAD)  
- Support‑oriented design and troubleshooting mindset  

---

# Purpose

This monorepo serves as a compact, practical demonstration of:

- Technical proficiency across the full support stack  
- Ability to build tools that improve reliability and reduce MTTR  
- Understanding of credit‑risk data flows  
- Experience designing clear, support‑friendly diagnostics  
- A structured, methodical approach to application support
