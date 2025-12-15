---

# 🚀 End-to-End Data Pipeline with Monitoring & Dashboard

This project demonstrates a **simple, reliable end-to-end data pipeline** that fetches data from a public API, transforms it, stores it in a SQL database, and visualizes it through a lightweight dashboard with basic monitoring and error logging.

The focus of this project is **reliability, automation readiness, and visibility**, not UI complexity.

---

## 📌 Architecture Overview

```
CoinGecko API
     ↓
Python Data Pipeline
     ↓
Data Transformation
     ↓
SQLite Database
     ↓
Monitoring & Logs
     ↓
HTML + JavaScript Dashboard
```

---

## 📊 API Used

**CoinGecko Public API**

* No API key required
* Reliable public cryptocurrency market data
* Real-world use case for aggregation and transformation

Example endpoint:

```
https://api.coingecko.com/api/v3/coins/markets
```

---

## 🛠 Tech Stack

* **Language:** Python 3
* **Database:** SQLite
* **Frontend:** HTML + JavaScript
* **Logging:** Python logging module
* **Environment:** Windows (local setup)

---

## 📁 Project Structure

```
pipeline-dashboard-data-logs/
│
├── pipeline/
│   ├── fetch_data.py        # Extract, transform, store, monitor
│   └── export_json.py       # Export DB data for dashboard
│
├── dashboard/
│   ├── index.html           # Dashboard UI
│   ├── script.js            # Fetch & render data
│   └── data.json            # Generated dashboard data
│
├── data/
│   └── crypto.db            # SQLite database
│
├── logs/
│   └── error.log            # Error logs
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Data Pipeline Flow

1. **Extraction**

   * Fetches top 10 cryptocurrencies by market cap from CoinGecko.
   * Handles API failures, timeouts, and invalid responses.

2. **Transformation**

   * Renames and normalizes fields.
   * Converts price from USD to INR.
   * Filters only required fields for storage.

3. **Storage**

   * Stores transformed data in SQLite.
   * Uses primary keys to avoid duplicates.
   * Pipeline is fully re-runnable.

4. **Monitoring**

   * Tracks last successful run time.
   * Stores pipeline status (`SUCCESS` / `FAILED`).
   * Logs errors to `logs/error.log`.

5. **Visualization**

   * Displays crypto prices and pipeline health.
   * Uses a lightweight HTML + JavaScript dashboard.

---

## 🚦 Monitoring & Reliability Features

* ✅ Error logging to file
* ✅ Pipeline status tracking
* ✅ Last successful execution timestamp
* ✅ Safe re-runs without duplicate data

---

## 🧪 Setup Instructions (Windows)

### 1️⃣ Clone the Repository

```bash
git clone <your-github-repo-url>
cd pipeline-dashboard-data-logs
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Data Pipeline

Run from the **project root directory**:

```bash
python pipeline\fetch_data.py
python pipeline\export_json.py
```

This will:

* Fetch & store crypto data
* Update pipeline status
* Generate `dashboard/data.json`

---

## 🌐 View the Dashboard

Due to browser security restrictions, the dashboard must be served via a local HTTP server.

```bash
cd dashboard
python -m http.server 8000
```

Open in browser:

```
http://localhost:8000
```

---

## 📈 Dashboard Displays

* Pipeline Status (SUCCESS / FAILED)
* Last Successful Run Time
* Cryptocurrency prices (USD & INR)
* Clean tabular visualization

---

## 🧠 Design Decisions

* **SQLite** chosen for simplicity and portability
* **JSON export** used to decouple backend from frontend
* **Local HTTP server** ensures secure data fetching
* **Relative paths** enable easy automation

---
## 🔁 Pipeline Automation

In production, this pipeline would be automated to run on a fixed schedule instead of being triggered manually.

* Cron / Task Scheduler
Schedule the pipeline to run at regular intervals (hourly or daily) using cron jobs (Linux) or Windows Task Scheduler.

* Cloud-Native Automation
Run the pipeline as an Azure Function or AWS Lambda with a timer trigger for serverless execution and automatic scaling.

* Workflow Orchestration
Use tools like n8n, Apache Airflow, or Azure Data Factory to manage retries, dependencies, and execution history.

* CI/CD Scheduling
Use GitHub Actions (cron workflows) to run the pipeline on a schedule and store logs as build artifacts.

---

## 🚨 Alerting & Notifications

To improve reliability and observability, alerting would be added for pipeline failures.

Send Slack notifications or email alerts when the pipeline status is marked as FAILED.

Trigger alerts via:

* Slack Webhooks

*IFTTT / Zapier Webhooks

* Cloud monitoring tools (Azure Monitor, AWS CloudWatch)

Alerts would include:

*Failure reason

* Timestamp

* Pipeline stage where the error occurred

---

## 📈 Production Improvements & Scalability

If this system were deployed in production, the following enhancements would be applied:

Replace SQLite with PostgreSQL or a managed cloud database for concurrency and scalability.

Add retry logic with exponential backoff for API calls.

Introduce centralized logging and metrics (ELK stack, Prometheus, Grafana).

Container orchestration using Kubernetes or Azure Container Apps.

Secure secrets using environment variables or a secrets manager.

Add API versioning and schema validation.

Implement role-based access control (RBAC) for the dashboard.

Enable horizontal scaling of ingestion and visualization components.

---

## ✅ Key Takeaway

This project shows how to build a **clean, reliable data pipeline** with **monitoring and visibility**, using simple tools that can easily scale to production systems.

---



