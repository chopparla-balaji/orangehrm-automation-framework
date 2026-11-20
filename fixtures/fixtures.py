import pytest
import threading
from utils.browser_factory import browser_init
from utils.constants import BROWSER

@pytest.fixture(scope="session")
def normal_driver(cross_browser):
    driver = browser_init(browser_name=cross_browser[BROWSER])
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def heal_driver(cross_browser):
    heal_driver = browser_init(browser_name=cross_browser[BROWSER], is_heal=True)
    yield heal_driver
    heal_driver.quit()


thread_local = threading.local()
@pytest.fixture(scope="function")
def thread_driver(cross_browser):
    if getattr(thread_local, "driver", None) is None:
        thread_local.driver = browser_init(browser_name=cross_browser[BROWSER])
    yield thread_local.driver
    thread_local.driver.quit()
    thread_local.driver = None


thread_heal_local = threading.local()
@pytest.fixture(scope="function")
def thread_heal_driver(cross_browser):
    if not hasattr(thread_heal_local, "driver"):
        thread_heal_local.driver = browser_init(browser_name=cross_browser[BROWSER], is_heal=True)
    yield thread_heal_local.driver
    thread_heal_local.driver.quit()
    del thread_heal_local.driver


"""
    variable_name = threading.local() (class type thread) (stores any data)
    variable_name.attribute_name = value
    access variable_name.attribute_name

    for parallel execution (threads) used so we use can function scope each test function follows thread system
 """