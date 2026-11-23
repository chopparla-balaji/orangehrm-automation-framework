import pytest
import threading
from utils.browser_factory import browser_init
from utils.constants import BROWSER


@pytest.fixture(scope="session")
def normal_driver(cross_browser):
    """
    Session-scoped fixture for normal WebDriver instance.
    Initializes browser once per session and reuses same instance.
    **Keywords**: driver, browser, session, initialization
    """
    driver = browser_init(browser_name=cross_browser[BROWSER])
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def heal_driver(cross_browser):
    """
    Session-scoped fixture for heal WebDriver instance with error recovery.
    Initializes browser once per session with auto-heal capabilities.
    **Keywords**: driver, browser, session, heal, error-recovery
    """
    heal_driver = browser_init(browser_name=cross_browser[BROWSER], is_heal=True)
    yield heal_driver
    heal_driver.quit()


thread_local = threading.local()


@pytest.fixture(scope="function")
def thread_driver(cross_browser):
    """
    Function-scoped fixture for thread-safe WebDriver instance.
    Uses thread-local storage for parallel test execution.
    **Keywords**: driver, browser, function, thread-safe, parallel
    """
    if getattr(thread_local, "driver", None) is None:
        thread_local.driver = browser_init(browser_name=cross_browser[BROWSER])
    yield thread_local.driver
    thread_local.driver.quit()
    thread_local.driver = None


thread_heal_local = threading.local()


@pytest.fixture(scope="function")
def thread_heal_driver(cross_browser):
    """
    Function-scoped fixture for thread-safe WebDriver with error recovery.
    Uses thread-local storage with auto-heal for parallel execution.
    **Keywords**: driver, browser, function, thread-safe, parallel, heal
    """
    if not hasattr(thread_heal_local, "driver"):
        thread_heal_local.driver = browser_init(browser_name=cross_browser[BROWSER], is_heal=True)
    yield thread_heal_local.driver
    thread_heal_local.driver.quit()
    del thread_heal_local.driver