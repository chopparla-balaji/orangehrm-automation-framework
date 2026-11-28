from typing import Final
from utils.type_checker import Locator
from pages.dashboard import Dashboard
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class UserMenu:

    ABOUT: Final[Locator] = (By.XPATH, "//header/descendant::ul[2]/descendant::li[1]/child::a")
    SUPPORT: Final[Locator] = (By.XPATH, "//header/descendant::ul[2]/descendant::li[2]/child::a")
    CHANGE_PASSWORD: Final[Locator] = (By.XPATH, "//header/descendant::ul[2]/descendant::li[3]/child::a")
    LOGOUT: Final[Locator] = (By.XPATH, "//header/descendant::ul[2]/descendant::li[4]/child::a")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def logout_orm(self) -> None:
        self.wait_for_user_menu_to_load()
        self.selenium_driver.element_click(self.LOGOUT)

    def wait_for_user_menu_to_load(self, is_landing:bool = True) -> None:
        if is_landing:
            self.selenium_driver.element_click(Dashboard.USER_DROP_DOWN)
        self.selenium_driver.wait_until_element_clickable(self.ABOUT)
        self.selenium_driver.wait_until_element_clickable(self.SUPPORT)
        self.selenium_driver.wait_until_element_clickable(self.CHANGE_PASSWORD)
        self.selenium_driver.wait_until_element_clickable(self.LOGOUT)
