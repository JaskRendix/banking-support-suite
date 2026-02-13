# Banking Data Pipeline — Credit Risk (ETL)

## Overview
This repository contains a compact, production‑style ETL pipeline for calculating **Risk‑Weighted Assets (RWA)** using standard Credit Risk parameters:

- **EAD** — Exposure at Default  
- **PD** — Probability of Default  
- **LGD** — Loss Given Default  

The pipeline mirrors the type of operational data processing performed within **BNP Paribas Finance & Risk Solutions**.

The core Basel‑style formula implemented is:

\[
RWA = EAD \times PD \times LGD \times 12.5
\]

---

## 🔍 Business Logic Highlights

### **Data Quality**
- Negative exposures are automatically filtered out.
- All transformations are logged for traceability.

### **Operational Reliability**
- Extraction failures (e.g., missing files) raise clear, support‑friendly errors.
- Logging provides a full audit trail of ETL steps.

### **Database Layer**
- Results are written to SQLite for demo purposes.
- `db_setup.sql` includes indexing to support large‑scale reporting workloads.

---

## 🚀 How to Run the Pipeline

### **1. Install the package (editable mode recommended during development)**

From the project root:

```bash
pip install -e banking_data_pipeline_python
```

This makes the `banking_data_pipeline` package importable from anywhere.

---

### **2. Run the ETL pipeline**

Because the project is now a proper Python package, you run it using the module syntax:

```bash
python -m banking_data_pipeline.rwa_calculator
```

This works from **any directory**, thanks to the `pathlib`‑based data resolution inside the script.

---

## Running Tests

Tests are located under:

```
banking_data_pipeline_python/tests/
```

Run them with:

```bash
pytest
```

All tests validate:

- RWA calculation correctness  
- Negative exposure filtering  
- Error handling for missing files  

---

## Project Structure

```
bnp/
│
├── banking_data_pipeline_python/
│   ├── banking_data_pipeline/
│   │   ├── rwa_calculator.py
│   │   ├── data/
│   │   │   └── mock_loans.csv
│   │   └── __init__.py
│   └── tests/
│       └── test_rwa_calculator.py
│
└── pyproject.toml
```

---

## 🛠️ Tech Stack

- **Python 3.11**
- **NumPy 1.26.4**
- **Pandas 2.1.4**
- **SQLite**
- **Pytest**

All versions are pinned in `pyproject.toml` for reproducibility.
