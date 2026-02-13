INSERT INTO transactions (transaction_ref, status, exposure_amount, error_code)
VALUES ('TX001', 'FAILED', 1200.50, 'ERR-42');

INSERT INTO transactions (transaction_ref, status, exposure_amount, error_code)
VALUES ('TX002', 'PROCESSED', 800.00, NULL);

INSERT INTO transactions (transaction_ref, status, exposure_amount, error_code)
VALUES ('TX003', 'FAILED', 450.00, 'MISSING_FX_RATE');
