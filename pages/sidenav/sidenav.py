from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class SideNav:

    SEARCH: Locator = (By.CSS_SELECTOR, "input[placeholder='Search'].oxd-input.oxd-input--active")
    ADMIN: Locator = (By.LINK_TEXT, "Admin")
    PIM: Locator = (By.LINK_TEXT, "PIM")
    LEAVE: Locator = (By.LINK_TEXT, "Leave")
    TIME: Locator = (By.LINK_TEXT, "Time")
    RECRUITMENT: Locator = (By.LINK_TEXT, "Recruitment")
    MY_INFO: Locator = (By.LINK_TEXT, "My Info")
    PERFORMANCE: Locator = (By.LINK_TEXT, "Performance")
    DASHBOARD: Locator = (By.LINK_TEXT, "Dashboard")
    CLAIM: Locator = (By.LINK_TEXT, "Claim")
    BUZZ: Locator = (By.LINK_TEXT, "Buzz")