from typing import Final
from utils.type_checker import Locator
from pages.common_page import CommonPage
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class UserMenu:

    ABOUT: Final[Locator] = (By.LINK_TEXT, "About")
    SUPPORT: Final[Locator] = (By.LINK_TEXT, "Support")
    CHANGE_PASSWORD: Final[Locator] = (By.LINK_TEXT, "Change Password")
    LOGOUT: Final[Locator] = (By.LINK_TEXT, "Logout")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def logout_orm(self) -> None:
        self.selenium_driver.element_click(CommonPage.USER_DROP_DOWN)
        self.selenium_driver.wait_until_element_present(self.ABOUT)
        self.selenium_driver.wait_until_element_present(self.CHANGE_PASSWORD)
        self.selenium_driver.wait_until_element_present(self.LOGOUT)
        self.selenium_driver.element_click(self.LOGOUT)
