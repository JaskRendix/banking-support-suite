# Banking Support Backend (Spring Boot)

A lightweight, production‑ready REST API built with **Java 17** and **Spring Boot**, designed to give Application Support teams fast visibility into failed risk‑engine transactions.

---

## Features

### Health Monitoring  
Quick endpoint to verify that the Support API is running and connected to the risk‑calculation layer.

### Failure Analysis  
Endpoints to retrieve all transactions or filter only those with status `FAILED`.

### H2 In‑Memory Database  
Perfect for local development and rapid prototyping. No installation required.

### Support‑Friendly Error Codes  
Each transaction includes an `errorCode` field (e.g., `MISSING_FX_RATE`, `INVALID_LIMIT`), allowing Support Technicians to diagnose issues without digging through logs.

---

## Project Structure

```
src/main/java/com/support
 ├── controller
 │    ├── SupportController.java
 │    └── TransactionController.java
 ├── model
 │    └── Transaction.java
 ├── repository
 │    └── TransactionRepository.java
 └── SupportPortalBackendApplication.java
```

---

## Prerequisites

- **Java 17**
- **Maven 3.8+**
- No external database required (H2 is embedded)

---

## Running the Application

From the project root:

```bash
mvn clean spring-boot:run
```

Spring Boot will start on:

```
http://localhost:8080
```

---

## Available Endpoints

### Health Check  
```
GET /api/support/health
```
Returns:
```
Support API is UP and connected to Risk Engine
```

### All Transactions  
```
GET /api/support/transactions
```

### Failed Transactions  
```
GET /api/support/transactions/failed
```

### Filter by Status  
```
GET /api/support/transactions/status/{status}
```

---

## Using the H2 Database

### Open the H2 Console  
Navigate to:

```
http://localhost:8080/h2-console
```

Use these settings:

| Field        | Value                     |
|--------------|---------------------------|
| JDBC URL     | `jdbc:h2:mem:supportdb`   |
| User         | `sa`                      |
| Password     | *(leave empty)*           |

---

## Insert Sample Data (for testing)

Run this inside the H2 console:

```sql
INSERT INTO transactions (transaction_ref, status, exposure_amount, error_code)
VALUES ('TX001', 'FAILED', 1200.50, 'ERR-42');

INSERT INTO transactions (transaction_ref, status, exposure_amount, error_code)
VALUES ('TX002', 'PROCESSED', 800.00, NULL);
```

Then call:

```
http://localhost:8080/api/support/transactions
```

You’ll now see real JSON output.

---

## Resetting the Database

Since H2 is in‑memory, simply restart the backend:

```bash
Ctrl + C
mvn spring-boot:run
```

The database resets automatically.

---

## Support Technician Mindset

This API is intentionally simple and explicit:

- **No hidden logic**
- **No complex joins**
- **No opaque error messages**

Every field exists to help Support teams answer one question:

> *“Why did this transaction fail?”*

The `errorCode` field is the key — it surfaces the root cause immediately.
