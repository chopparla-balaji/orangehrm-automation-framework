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
├── base/                          # Base classes for driver and page objects
│   ├── base_driver.py            # Base driver class with common methods
│   └── selenium_driver.py        # Selenium WebDriver implementation
│
├── pages/                         # Page Object Model (POM) classes
│   ├── common_page.py            # Common methods used across pages
│   ├── login_page.py             # Login page object
│   ├── usermenu.py               # User menu page object
│   ├── sidenav/                  # Side navigation pages
│   │   ├── dashboard.py          # Dashboard page
│   │   ├── sidenav.py            # Main sidenav component
│   │   └── admin/                # Admin section pages
│   │       ├── system_users.py   # System users management
│   │       └── user_management.py # User management page
│   └── ...
│
├── tests/                         # Test cases
│   ├── conftest.py               # Pytest configuration and fixtures
│   ├── sample_test.py            # Sample test examples
│   ├── user_management_test.py   # User management tests
│   └── ...
│
├── fixtures/                      # Test fixtures
│   └── fixtures.py               # Reusable test fixtures
│
├── utils/                         # Utility modules
│   ├── browser_factory.py        # Browser initialization factory
│   ├── constants.py              # Application constants
│   ├── page_titles.py            # Page titles reference
│   ├── testdata.py               # Test data management
│   └── type_checker.py           # Type checking utilities
│
├── docker-compose.yml            # Docker services configuration
├── requirements.txt              # Python dependencies (Selenium, pytest, Healenium, etc.)
├── pytest.ini                    # Pytest configuration
├── conftest.py                   # Global pytest configuration
├── README.md                     # This file (documentation)
├── .gitignore                    # Git ignore rules (excludes __pycache__, .env, test reports, etc.)
└── .env.example                  # Example environment variables (copy to .env)
```

### **Key Directory Descriptions:**

| Directory | Purpose |
|-----------|---------|
| `base/` | Base classes with Selenium WebDriver initialization and common methods |
| `pages/` | Page Objects following POM pattern for each application page |
| `tests/` | Test scripts organized by feature/module |
| `fixtures/` | Reusable test fixtures and setup/teardown logic |
| `utils/` | Helper utilities for constants, test data, and browser management |

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
pytest tests/user_management_test.py

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

### **Local Execution**

```bash
# Simple test run
pytest tests/

# With detailed output
pytest tests/ -v -s

# With specific test
pytest tests/user_management_test.py::test_create_user -v

# Generate HTML report
pytest tests/ --html=report.html --self-contained-html
```

### **Test Organization**

Tests are organized using:
- **Test files:** `*_test.py` pattern in `tests/` directory
- **Test classes:** Group related tests
- **Test methods:** `test_*` naming convention
- **Fixtures:** Defined in `conftest.py`

### **Example Test Structure**

```python
class TestUserManagement:
    def test_create_user(self, driver):
        # Setup
        login_page = LoginPage(driver)
        
        # Execute
        login_page.login("admin", "password")
        user_mgmt = UserManagementPage(driver)
        user_mgmt.create_user("John Doe", "john@example.com")
        
        # Assert
        assert user_mgmt.is_user_created("John Doe")
```

---

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

# View real-time logs
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

### **Jenkins Integration with Healenium**

1. Access Jenkins: http://localhost:8080
2. Create new Pipeline job
3. Add pipeline script:
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Run Tests with Healenium') {
               steps {
                   sh '''
                   pip install -r requirements.txt
                   pytest tests/ -v --html=report.html --junitxml=results.xml
                   '''
               }
           }
       }
       post {
           always {
               publishHTML([
                   reportDir: '.',
                   reportFiles: 'report.html',
                   reportName: 'Test Report'
               ])
           }
       }
   }
   ```
4. Schedule builds for automated testing

---

## Configuration

### **Environment Variables**

Create `.env` file in project root:

```env
BASE_URL=http://localhost:8080
BROWSER=chrome
HEADLESS=true
TIMEOUT=10
HEALENIUM_ENABLED=true
HEALENIUM_PROXY=http://localhost:8085
```

### **Page Titles Reference**

Defined in `utils/page_titles.py`:

```python
DASHBOARD_TITLE = "Dashboard"
LOGIN_TITLE = "Login"
USER_MANAGEMENT_TITLE = "User Management"
```

### **Test Data**

Manage test data in `utils/testdata.py`:

```python
TEST_USERS = {
    "admin": {"username": "admin", "password": "admin123"},
    "user": {"username": "user", "password": "user123"}
}
```

---

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

**Last Updated:** 2026-11-25

