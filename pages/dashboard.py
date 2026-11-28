from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.sidenav_page import SideNav


class Dashboard:

    TIME_AT_WORK: Final[Locator] = (By.XPATH, "//hr[@role='separator']/parent::div")
    MY_ACTIONS: Final[Locator] = (By.XPATH, "(//hr[@role='separator'])[3]/parent::div")
    QUICK_LAUNCH: Final[Locator] = (By.XPATH, "(//hr[@role='separator'])[4]/parent::div")
    BUZZ_LATEST_POSTS: Final[Locator] = (By.XPATH, "(//hr[@role='separator'])[5]/parent::div")
    USER_DROP_DOWN: Final[Locator] = (By.CSS_SELECTOR, "header div:nth-child(1) div:nth-child(3) > ul > li "
                                                       "span:nth-child(1)")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def wait_for_dashboard_to_load(self) -> None:
        self.selenium_driver.wait_until_element_clickable(SideNav.SIDE_NAV_INDICATOR)
        self.selenium_driver.wait_until_element_present(self.USER_DROP_DOWN)
        self.selenium_driver.wait_until_element_present(self.TIME_AT_WORK)
        self.selenium_driver.wait_until_element_present(self.MY_ACTIONS)
        self.selenium_driver.wait_until_element_present(self.QUICK_LAUNCH)
        self.selenium_driver.wait_until_element_present(self.BUZZ_LATEST_POSTS)
        self.selenium_driver.validate_page_title()
