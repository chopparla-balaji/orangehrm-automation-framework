from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from utils.constants import ORANGE_HRM_URL, ADMIN_USERNAME, ADMIN_PASSWORD


class LoginPage:

    USERNAME: Final[Locator] = (By.NAME, "username")
    PASSWORD: Final[Locator] = (By.NAME, "password")
    LOGIN_BTN: Final[Locator] = (By.XPATH, "//button[@type='submit']")
    FORGOT_YOUR_PASSWORD: Final[Locator] = (By.XPATH, "//button[@type='submit']/following::p[1]")
    ORANGE_HRM_INC: Final[Locator] = (By.LINK_TEXT, "OrangeHRM, Inc")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def open_orangehrm(self) -> None:
        self.selenium_driver.open_url(ORANGE_HRM_URL)
        self.validate_login_page()

    def enter_credentials(self) -> None:
        self.selenium_driver.send_keys(self.USERNAME, ADMIN_USERNAME)
        self.selenium_driver.send_keys(self.PASSWORD, ADMIN_PASSWORD)

    def validate_login_page(self) -> None:
        self.selenium_driver.wait_until_element_present(self.USERNAME)
        self.selenium_driver.wait_until_element_present(self.PASSWORD)
        self.selenium_driver.validate_page_title()
