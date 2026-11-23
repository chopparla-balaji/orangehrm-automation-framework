import pytest
from pages.login_page import LoginPage
from pages.sidenav.dashboard import Dashboard
from base.selenium_driver import SeleniumDriver
from utils.constants import (BROWSER_CL, IS_PARALLEL_CL, IS_NORMAL_DRIVER_CL, BROWSER, IS_PARALLEL, IS_NORMAL_DRIVER,
                             FIREFOX, CHROME, EDGE, TRUE_STR, FALSE_STR, STORE)

from fixtures.fixtures import normal_driver, heal_driver, thread_driver, thread_heal_driver
# pytest_plugins = ["fixtures.fixtures.normal_driver", "", ""] [Alternative way to load fixtures from other modules]

def pytest_addoption(parser):
    parser.addoption(BROWSER_CL, action=STORE, choices=(CHROME, FIREFOX,EDGE), default=FIREFOX)
    parser.addoption(IS_NORMAL_DRIVER_CL, action=STORE, default=FALSE_STR, choices=(TRUE_STR, FALSE_STR))
    parser.addoption(IS_PARALLEL_CL, action=STORE, default=FALSE_STR, choices=(TRUE_STR, FALSE_STR))

@pytest.fixture(scope="session")
def cross_browser(request):
    return {
            BROWSER: request.config.getoption(BROWSER_CL),
            IS_NORMAL_DRIVER: request.config.getoption(IS_NORMAL_DRIVER_CL) == TRUE_STR,
            IS_PARALLEL: request.config.getoption(IS_PARALLEL_CL) == TRUE_STR,
            }

@pytest.fixture(scope="function")
def driver_initialization(request, cross_browser):
    is_normal_driver = cross_browser[IS_NORMAL_DRIVER]
    is_parallel = cross_browser[IS_PARALLEL]
    if not is_parallel:
        fixture_name = "normal_driver" if is_normal_driver else "heal_driver"
    else:
        fixture_name = "thread_driver" if is_normal_driver else "thread_heal_driver"

    return request.getfixturevalue(fixture_name)

@pytest.fixture(scope="function")
def selenium_driver(driver_initialization):
    return SeleniumDriver(driver_initialization)

@pytest.fixture(scope="function")
def login_in(selenium_driver):
    login_page = LoginPage(selenium_driver)
    login_page.open_orangehrm()
    login_page.enter_credentials()
    login_page.selenium_driver.element_click(login_page.LOGIN_BTN)
    dashboard = Dashboard(selenium_driver)
    dashboard.validate_dashboard()
