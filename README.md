# OrangeHRM Automation Framework

Enterprise-grade Selenium 4 test automation with self-healing locators, POM architecture, and CI/CD pipeline - built for real-world HR workflows.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.15-43B02A?style=flat-square&logo=selenium&logoColor=white)
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
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Docker Services](#docker-services)
- [CI/CD](#cicd)

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
│   ├── user_menu.py
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
│   ├── shared_resources.py
│   └── ui_helpers.py
├── docker-compose.yml
├── requirements.txt
├── conftest.py           # CLI options, selenium_driver, login_in, log_out fixtures
├── README.md
├── .gitignore
└── .env.example
```

---

## Setup

### **1. Clone Repository & Install Dependencies**

```bash
git clone <repository-url>
cd orangehrm-automation-framework

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Or (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **2. Start Docker Services (Optional - for Healenium)**

```bash
docker-compose pull
docker-compose up -d
docker-compose ps
```

Services running:
- PostgreSQL 14 (Port 5432)
- Healenium Backend (Port 7878)
- Healenium Proxy (Port 8085)

---

## Running Tests

### **Normal Driver (Public Demo - Sequential)**

```bash
# Run all tests
python -m pytest tests/ --is_normal_driver true --browser_type chrome -v

# Run specific test
python -m pytest tests/admin/test_admin_web_elements_waits.py --is_normal_driver true --browser_type chrome -v

# Generate HTML report
python -m pytest tests/ --is_normal_driver true --browser_type chrome --html=report.html
```

### **Healenium Driver (Self-Healing)**

```bash
# Start Docker services
docker-compose up -d

# Run with Healenium
python -m pytest tests/ --is_normal_driver false --browser_type chrome -v
```

### **Thread Driver (Parallel Execution)**

```bash
# Run tests in parallel (requires local OrangeHRM instance)
python -m pytest tests/ --is_normal_driver true --is_parallel true --browser_type chrome -v
```

### **CLI Arguments**

| Argument | Values | Default | Purpose |
|----------|--------|---------|---------|
| `--browser_type` | `chrome`, `firefox`, `edge` | `firefox` | Browser type |
| `--is_normal_driver` | `true`, `false` | `false` | Selenium (true) or Healenium (false) |
| `--is_parallel` | `true`, `false` | `false` | Parallel execution |

---

## Docker Services

### **Services**

| Service | Image | Port | URL |
|---------|-------|------|-----|
| PostgreSQL | postgres:14 | 5432 | localhost:5432 |
| Healenium Backend | healenium/hlm-backend:3.5.1 | 7878 | http://localhost:7878 |
| Healenium Proxy | healenium/hlm-proxy:3.0.6 | 8085 | http://localhost:8085 |

### **Quick Commands**

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f healenium-backend
docker-compose logs -f healenium-proxy

# Stop all services
docker-compose down

# Stop and remove data
docker-compose down -v

# Check status
docker-compose ps

# Wait for services (~60 seconds), then test
curl http://localhost:7878/health
curl http://localhost:8085/health
```

### **Access Services**

| Service | URL | Purpose |
|---------|-----|---------|
| Healenium Backend | http://localhost:7878 | Healing engine API |
| Healenium Proxy | http://localhost:8085 | WebDriver proxy for self-healing |
| PostgreSQL | localhost:5432 | Database (Healenium storage) |

### **Test Healenium**

After starting Docker services, run tests with Healenium:

```bash
# Run with Healenium self-healing
python -m pytest tests/ --is_normal_driver false --browser_type chrome -v
```

Healenium will automatically heal broken XPaths via http://localhost:8085

---

## CI/CD

The deployment pipeline is maintained in a dedicated repository (SCM separation of test code and deployment config):

**[orangehrm-automation-deployment](https://github.com/chopparla-balaji/orangehrm-automation-deployment)**

The pipeline checks out this framework, installs dependencies, and runs the test suite.

---

**Last Updated:** 2026-11-28

