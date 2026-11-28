# OrangeHRM Automation Framework

Enterprise-grade Selenium 4 test automation with self-healing locators, POM architecture, and CI/CD pipeline — built for real-world HR workflows.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.0-43B02A?style=flat-square&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-latest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Healenium](https://img.shields.io/badge/Healenium-SelfHealing-blueviolet?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat-square&logo=github-actions&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Reports-orange?style=flat-square&logo=qase&logoColor=white)

---

## Table of Contents

- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [End-to-End Setup Steps](#end-to-end-setup-steps)
- [Running Tests](#running-tests)
- [Docker Services](#docker-services)
- [Configuration](#configuration)

---

## Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd orangehrm-automation-framework

# Install dependencies
pip install -r requirements.txt

# Start Docker services
docker-compose up -d

# Run tests
pytest tests/

# View reports
allure serve allure-results
```

---

## Key Features

- **Page Object Model** - Organized page classes for maintainability
- **Multi-language Support** - Attribute-based XPaths (not text-dependent)
- **Self-Healing** - Automatic locator recovery with Healenium
- **Parallel Execution** - Thread-safe fixtures for running tests in parallel
- **Docker Integration** - Pre-configured Healenium stack

---

## Prerequisites

- **Python 3.11+**
- **Git**
- **Docker & Docker Desktop**
- **pip** (Python package manager)
- **Chrome/Firefox browser** (for local testing)

---

## Project Structure

```
orangehrm-automation-framework/
├── base/                 # Abstract base driver (Selenium WebDriver)
│   ├── base_driver.py    # Abstract class with common methods
│   └── selenium_driver.py # Concrete implementation
├── pages/                # Page Objects (final + type checked)
│   ├── login_page.py
│   ├── dashboard.py
│   ├── change_password.py
│   ├── reset_password.py
│   ├── usermenu.py
│   ├── sidenav_page.py
│   └── sidenav/
│       ├── admin/, claim.py, performance.py, recruitment.py, time_sheet.py
│       └── leave/, my_info/, pim/
├── tests/                # Test Cases
│   ├── test_sample.py
│   └── admin/, claim/, leave/, my_info/, password/, performance/, pim/, recruitment/, time_sheet/
├── fixtures/             # Fixtures (normal, thread-safe, Healenium)
│   └── fixtures.py       # normal_driver, heal_driver, thread_driver, thread_heal_driver
├── utils/                # Utilities
│   ├── browser_factory.py # Browser init (Chrome/Firefox/Edge, Healenium support)
│   ├── constants.py
│   ├── page_titles.py
│   ├── testdata.py
│   ├── type_checker.py
│   └── utils.py
├── docker-compose.yml
├── requirements.txt
├── conftest.py           # CLI options, selenium_driver, login_in, log_out fixtures
├── README.md
├── .gitignore
└── .env.example
```

---

## End-to-End Setup Steps

### **Step 1: Clone & Setup Project**

```bash
# Clone the repository
git clone <repository-url>
cd orangehrm-automation-framework

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### **Step 2: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 3: Start Docker Services**

```bash
# Pull all required Docker images
docker-compose pull

# Start all services in background
docker-compose up -d

# Verify services are running
docker ps
```

**Services Started:**
- PostgreSQL (Port 5432) - Database for Healenium
- Healenium Backend (Port 7878) - Self-healing backend
- Healenium Proxy (Port 8085) - Self-healing proxy
- Jenkins (Port 8080) - CI/CD automation

### **Step 4: Configure Test Environment**

Update configuration in `utils/constants.py`:

```python
# Browser configuration
BASE_URL = "http://localhost:8080"  # OrangeHRM URL
BROWSER_TYPE = "chrome"  # or "firefox"

# Healenium configuration (optional)
USE_HEALENIUM = True
HEALENIUM_PROXY_URL = "http://localhost:8085"
```

### **Step 5: Run Tests Locally**

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_admin_web_elements_waits.py

# Run with verbose output
pytest tests/ -v

# Run with markers
pytest tests/ -m "login"

# Run with Healenium self-healing
pytest tests/ --healenium
```

### **Step 6: Generate Reports**

```bash
# Generate Allure report
pytest tests/ --alluredir=allure-results

# View report
allure serve allure-results
```

### **Step 7: Access Jenkins (Optional)**

```
Jenkins Dashboard: http://localhost:8080
Healenium Dashboard: http://localhost:8085
```

---

## Running Tests

### **Local Execution (Normal Selenium Driver)**

```bash
# Run full test suite against live demo
python -m pytest --is_normal_driver true --browser_type chrome -v

# Run specific test module
python -m pytest tests/admin/test_admin_web_elements_waits.py --is_normal_driver true --browser_type chrome -v

# Run with detailed output
python -m pytest tests/ --is_normal_driver true --browser_type chrome -v -s

# Generate HTML report
python -m pytest tests/ --html=report.html --self-contained-html
```

### **Running Tests with Healenium (Self-Healing)**

```bash
# Start Docker services first
docker-compose up -d

# Run tests with Healenium (default driver)
python -m pytest tests/ --is_normal_driver false -v

# Tests will auto-heal broken XPaths via http://localhost:8085
```

### **Command-Line Options**

| Option | Values | Default | Purpose |
|--------|--------|---------|---------|
| `--browser_type` | `chrome`, `firefox`, `edge` | `firefox` | Browser to use for testing |
| `--is_normal_driver` | `true`, `false` | `false` | Use Selenium (true) or Healenium (false) |
| `--is_parallel` | `true`, `false` | `false` | Run tests in parallel with xdist |


## Docker Services (Healenium Stack)

### **Architecture Overview**

This project uses **Healenium Self-Healing Framework** with Docker for:
- **Auto XPath Healing** - Automatically detects and fixes broken locators
- **Self-Learning AI** - Improves accuracy with every test run
- **Centralized Reporting** - Track all healing events and test results

### **Service Details**

| Service | Image | Port | Purpose |
|---------|-------|------|---------|
| **PostgreSQL** | postgres:14 | 5432 | Store Healenium metrics & healing data |
| **Healenium Backend** | healenium/hlm-backend:4.0.2 | 7878 | AI-powered healing engine |
| **Healenium Proxy** | healenium/hlm-proxy:2.3.0 | 8085 | WebDriver proxy for XPath interception |
| **Jenkins** | jenkins/jenkins:lts | 8080 | CI/CD pipeline automation |

### **Docker Setup Instructions**

**Prerequisites:**
```bash
# Docker Desktop running
# Minimum 4GB RAM for Docker
# 5GB free disk space
```

**Step 1: Pull latest images**
```bash
docker-compose pull
```

**Step 2: Start all services**
```bash
docker-compose up -d
```

**Step 3: Verify services are running**
```bash
docker ps

# Should show 4 containers: healenium-db, healenium-backend, healenium-proxy, jenkins
```

**Step 4: Wait for services to be ready (~30 seconds)**
```bash
docker-compose logs -f

# Wait for messages like "Started" and health checks passing
```

### **Accessing Services**

```
Jenkins:              http://localhost:8080
Healenium UI:         http://localhost:8085
Healenium API:        http://localhost:8085/api
PostgreSQL:           localhost:5432
```

### **Docker Commands**

```bash
# Start services in background
docker-compose up -d

# View real-time_sheet logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f healenium-backend
docker-compose logs -f healenium-proxy
docker-compose logs -f jenkins

# Stop all services (data persists)
docker-compose down

# Stop and remove all data
docker-compose down -v

# Restart specific service
docker-compose restart healenium-backend

# Check service health status
docker-compose ps

# View resource usage
docker stats
```

### **Running Tests with Healenium**

The Healenium Proxy at `localhost:8085` automatically intercepts WebDriver commands:

```bash
# 1. Start Docker services
docker-compose up -d

# 2. Run tests (they'll auto-heal via proxy)
pytest tests/ -v

# 3. When an XPath breaks, Healenium automatically:
#    - Detects the failure
#    - Suggests alternative selectors using AI
#    - Applies fix automatically or logs for review
```

**Example Test with Self-Healing:**

```python
# Your tests work normally - Healenium handles healing transparently
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://target-app.com")

# If this XPath breaks in the app, Healenium heals it automatically:
element = driver.find_element("xpath", "//button[@id='submit']")
element.click()
```

### **Troubleshooting Docker Issues**

```bash
# If services fail to start:
docker-compose logs healenium-backend

# If ports are already in use:
netstat -ano | findstr :7878
netstat -ano | findstr :8085

# Reset everything:
docker-compose down -v
docker-compose pull
docker-compose up -d
```

## Architecture

### **Page Object Model (POM)**

Each page has its own class:
- Encapsulates locators and actions
- Reusable across test cases
- Easy maintenance and updates

### **Self-Healing with Healenium**

Automatically detects XPath changes:
- Reduces test maintenance
- Improves test stability
- Logs healing events

### **CI/CD Pipeline**

Jenkins integration for:
- Automated test execution
- Scheduled test runs
- Report generation and distribution

---

## Troubleshooting

### **Docker Issues**

```bash
# Docker daemon not running
# Solution: Start Docker Desktop

# Image not found
docker-compose pull

# Port already in use
docker-compose down -v
docker-compose up -d
```

### **Test Failures**

- Check element locators in page objects
- Verify test data is correct
- Review browser console logs
- Check Healenium reports

---

## Support & Contributing

For issues or contributions, please open a GitHub issue or submit a pull request.

---

**Last Updated:** 2026-11-28

