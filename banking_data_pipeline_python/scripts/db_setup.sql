-- Database schema for Credit Risk Reporting
​CREATE TABLE IF NOT EXISTS risk_reports (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    loan_id TEXT NOT NULL,
    customer_name TEXT,
    ead REAL, -- Exposure at Default
    pd REAL, -- Probability of Default
    lgd REAL, -- Loss Given Default
    rwa REAL, -- Risk Weighted Assets
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexing for performance on high-volume queries
CREATE INDEX IF NOT EXISTS idx_loan_id ON risk_reports (loan_id);