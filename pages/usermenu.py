from typing import Final
from utils.type_checker import Locator
from pages.common_page import CommonPage
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
        self.selenium_driver.element_click(CommonPage.USER_DROP_DOWN)
        self.selenium_driver.wait_until_element_present(self.ABOUT)
        self.selenium_driver.wait_until_element_present(self.CHANGE_PASSWORD)
        self.selenium_driver.wait_until_element_present(self.LOGOUT)
        self.selenium_driver.element_click(self.LOGOUT)
