# MLOps Lab 2

## Project Overview

This project demonstrates an end-to-end MLOps workflow for a modular Python application. The lab focuses on environment isolation, structured code organization, automated testing, and CI integration using GitHub Actions.

A calculator module was implemented and validated using two testing frameworks: **Pytest** and **Unittest**, with automated test execution configured via CI pipelines.

---

## Objectives

- Create and manage a Python virtual environment
- Structure a project using modular design (`src`, `test`)
- Implement automated testing using Pytest and Unittest
- Configure CI workflows using GitHub Actions
- Generate and upload automated test reports

---

## Implementation Details

### 1️Modular Code Design

The calculator module (`src/calculator.py`) contains:

- `fun1(x, y)` → Addition
- `fun2(x, y)` → Subtraction
- `fun3(x, y)` → Multiplication
- `fun4(x, y, z)` → Sum of three numbers

---

## Custom Enhancements (My Contributions)

The original lab template was extended with the following improvements:

### 1. Centralized Input Validation

Instead of repeating type checks in every function, I implemented a reusable validation function:
```python
def validate_numbers(*args):
    if not all(isinstance(i, (int, float)) for i in args):
        raise ValueError("All inputs must be numbers.")
```

This improves:
- Code maintainability
- Reusability
- Clean architecture

### 2. Added Exception Handling Tests

I added test cases to verify that invalid inputs correctly raise `ValueError`.

**Example (Pytest):**
```python
def test_invalid_input():
    with pytest.raises(ValueError):
        calculator.fun1("a", 2)
```

This ensures robust input validation and improves test coverage.

### 3. Dual Testing Framework Implementation

The project supports:
- **Pytest** (function-based testing)
- **Unittest** (class-based testing)

This demonstrates understanding of both testing styles and improves reliability.

### 4. Automated CI Workflows

Two separate GitHub Actions workflows were created:
- `pytest_action.yml`
- `unittest_action.yml`

Each workflow:
- Triggers on push to `main`
- Sets up Python environment
- Installs dependencies
- Runs tests
- Generates test reports (Pytest XML report)
- Uploads test artifacts

---

## ⚙️ How to Run This Project Locally

### Step 1: Clone Repository
```bash
git clone 
cd mlops-lab1-calculator
```

### Step 2: Create Virtual Environment
```bash
python -m venv lab_01
```

**Activate:**

- **Mac/Linux:**
```bash
  source lab_01/bin/activate
```
- **Windows:**
```bash
  lab_01\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Pytest
```bash
pytest
```

### Step 5: Run Unittest
```bash
python -m unittest discover -s test
```

---

## Continuous Integration (CI)

The CI pipeline is implemented using GitHub Actions.

**On every push to the `main` branch:**
- Code is automatically checked out
- Python environment is configured
- Dependencies are installed
- Tests are executed
- Results are reported

If any test fails, the workflow is marked as failed. This ensures code quality before integration or collaboration.

---

## Why This Matters in MLOps

This lab demonstrates core MLOps principles:
- **Reproducible environments**
- **Automated testing**
- **CI automation**
- **Structured modular development**
- **Code validation and robustness**

These practices form the foundation for scalable ML systems in production environments.

---

## Author

**Moumita Baidya**  
Master's in Data Science
