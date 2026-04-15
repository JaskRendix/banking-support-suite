# **Application Support Portfolio — Full‑Stack Banking Operations**

This repository contains four independent projects that reflect the core responsibilities of Application Support in banking: data processing, operational diagnostics, backend visibility, and user‑facing support tools.  
Each module is self‑contained and demonstrates a specific capability used in daily support work.

---

# Repository Structure

```
/
├── banking_data_pipeline_python/     # Credit Risk ETL (Python)
├── it_ops_automation_toolkit/        # Shell + Python Ops Tools
├── support_portal_backend/           # Spring Boot Support API
└── support_portal_frontend/          # Angular Support Portal UI
```

---

# Project Overview

## **1. Credit Risk ETL Pipeline (Python)**  
A modular ETL that computes **Risk‑Weighted Assets (RWA)** using standard credit‑risk inputs (EAD, PD, LGD).  
Includes data‑quality checks, structured logging, error handling, and SQLite output for traceability.

**Run:**
```bash
pip install -e banking_data_pipeline_python
python -m banking_data_pipeline.rwa_calculator
```

---

## **2. IT Ops & Automation Toolkit**  
A collection of operational tools used for routine checks and incident triage.

- `health_check.sh` — process, disk, and file monitoring  
- `log_analyzer.py` — log parsing with WARN/ERROR/FATAL extraction  

These scripts model real support workflows: control points, environment checks, and fast diagnostics.

---

## **3. Support Portal Backend (Spring Boot, Java 17)**  
A REST API that exposes transaction data and failure causes for support teams.  
Provides health checks, filtering endpoints, and an H2 in‑memory database for local analysis.

**Run:**
```bash
mvn clean spring-boot:run
```

### Test Suite  
The backend includes a **MockMvc + Mockito** test suite for API‑contract validation.  
Tests use `@WebMvcTest` to isolate the web layer:

- Controllers and HTTP mappings only  
- Repository and service layers mocked  
- No database or full Spring context  

This enforces **Separation of Concerns** and ensures stable, predictable responses for support workflows.

---

## **4. Support Portal Frontend (Angular)**  
A simple UI that displays system health and failed transactions.  
Designed to give support teams a clear view of backend status and failure patterns.

**Run:**
```bash
ng serve
```

---

# End‑to‑End Flow

The four modules form a compact support ecosystem:

1. **ETL pipeline** processes credit‑risk data.  
2. **Ops toolkit** monitors the environment and inspects logs.  
3. **Backend API** exposes diagnostic information.  
4. **Frontend UI** presents it to support teams.

This mirrors the operational lifecycle of a banking application:  
**data → monitoring → diagnostics → visibility**.

---

# Skills Demonstrated

- Python (ETL, validation, logging)  
- SQL (SQLite, H2)  
- Java (Spring Boot, REST APIs)  
- Angular (TypeScript)  
- Shell scripting  
- Operational diagnostics and log analysis  
- Credit‑risk fundamentals (RWA, PD, LGD, EAD)  
- Support‑oriented API and tooling design  

---

# Purpose

This monorepo demonstrates:

- Breadth across backend, frontend, ETL, and operational tooling  
- Ability to design systems that reduce MTTR and improve visibility  
- Clear diagnostic surfaces for support teams  
- Structured, maintainable engineering aligned with support requirements  
