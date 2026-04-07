# Zeahire Automation Test Suite (Playwright + Pytest)

---

## 📌 Overview

This repository contains automated end-to-end smoke and regression tests
for the Zeahire web application.

The primary objective of this suite is to:

- Validate critical business workflows
- Provide deployment confidence
- Detect UI/API breakages early
- Integrate seamlessly with Azure DevOps CI pipeline

---

## 🧰 Tech Stack

- Python 3.12
- Playwright (Python)
- Pytest
- Allure Reporting
- JUnit XML (CI Integration)
- Page Object Model (POM Architecture)

---

## 📂 Project Structure

```
Zeahire_automation_playwright/
│
├── pages/                     # Page Object Models
│   ├── schedule_interview_page.py
│   ├── create_job_page.py
│   └── ...
│
├── tests/                     # Test Cases
│   ├── test_schedule_interview_smoke.py
│   ├── test_resume_parsing_smoke.py
│   ├── test_create_job.py
│   └── ...
│
├── reports/                   # Generated test artifacts (ignored in git)
│   ├── junit.xml
│   ├── allure-results/
│   ├── allure-report/
│   └── traces/
│
├── conftest.py                # Fixtures & Hooks
├── pytest.ini                 # Pytest configuration
├── requirements.txt
└── README.md
```

---

## 🚀 Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

## ▶️ Running Tests

### Run Smoke Suite

```bash
pytest -m smoke
```

This will:
- Execute smoke tests
- Generate JUnit report at `reports/junit.xml`

---

## 📊 Generate Allure Report (Local Debugging)

### Step 1 — Run Tests with Allure

```bash
pytest -m smoke --alluredir=reports/allure-results --pw-trace
```

### Step 2 — Open Allure Report

```bash
allure serve reports/allure-results
```

This provides:
- Failure screenshots
- Playwright traces
- Execution history
- Detailed debugging view

---

## 📦 CI Integration (Azure DevOps)

The suite generates:

- `reports/junit.xml` → Used by Azure DevOps Test Results
- `reports/allure-results/` → Used to generate Allure report
- `reports/traces/` → Playwright debugging traces

JUnit XML enables native CI dashboard integration.
Allure provides deep debugging insights.

---

## 🏷️ Test Markers

```
@pytest.mark.smoke
@pytest.mark.regression
```

Run specific suite:

```bash
pytest -m smoke
pytest -m regression
```

---

## 🔐 Environment Variables

Credentials and environment configs can be overridden using:

```bash
export BASE_URL=https://qa.zeahire.ai
export EMAIL=your_email
export PASSWORD=your_password
export HEADLESS=true
```

---

## 🧪 Reporting Strategy

| Tool | Purpose |
|------|----------|
| JUnit XML | CI Dashboard Summary |
| Allure | Detailed Failure Analysis |
| Playwright Trace | Deep UI Debugging |
| Screenshots | Failure Evidence |

---

## 🔮 Future Enhancements

- Externalized test data
- Parallel execution
- API layer integration
- Pipeline history tracking
- Environment metadata in Allure

---

## 👤 Maintainer

QA Automation Engineer – Zeahire Project  
Focused on building stable, CI-ready automation for deployment validation.