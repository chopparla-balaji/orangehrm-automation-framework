from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.login_page import LoginPage

class ResetPassword:

    USERNAME: Final[Locator] = (By.NAME, "username")
    CANCEL: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='button']")
    RESET_PASSWORD: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='submit']")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def wait_for_reset_password_to_load(self, is_landing_page: bool=True) -> None:
        login_page = LoginPage(self.selenium_driver)
        if is_landing_page:
            login_page.selenium_driver.element_click(login_page.FORGOT_YOUR_PASSWORD)
        self.selenium_driver.wait_until_element_present(self.USERNAME)
        self.selenium_driver.wait_until_element_clickable(self.CANCEL)
        self.selenium_driver.wait_until_element_clickable(self.RESET_PASSWORD)
