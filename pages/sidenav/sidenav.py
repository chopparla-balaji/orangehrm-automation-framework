from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class SideNav:

    SEARCH: Final[Locator] = (By.CSS_SELECTOR, "input[placeholder='Search'].oxd-input.oxd-input--active")
    ADMIN: Final[Locator] = (By.LINK_TEXT, "Admin")
    PIM: Final[Locator] = (By.LINK_TEXT, "PIM")
    LEAVE: Final[Locator] = (By.LINK_TEXT, "Leave")
    TIME: Final[Locator] = (By.LINK_TEXT, "Time")
    RECRUITMENT: Final[Locator] = (By.LINK_TEXT, "Recruitment")
    MY_INFO: Final[Locator] = (By.LINK_TEXT, "My Info")
    PERFORMANCE: Final[Locator] = (By.LINK_TEXT, "Performance")
    DASHBOARD: Final[Locator] = (By.LINK_TEXT, "Dashboard")
    CLAIM: Final[Locator] = (By.LINK_TEXT, "Claim")
    BUZZ: Final[Locator] = (By.LINK_TEXT, "Buzz")