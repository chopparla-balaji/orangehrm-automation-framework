from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.usermenu import UserMenu
from pages.common_page import CommonPage

class ChangePassword:

    CURRENT_PASSWORD : Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    PASSWORD: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    CONFIRM_PASSWORD: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    CANCEL: Final[Locator] = (By.XPATH, "//button[@type='button']")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")

    def __init__(self, selenium_driver: SeleniumDriver):
        self.selenium_driver = selenium_driver

    def wait_for_change_password_to_load(self):
        user_menu = UserMenu(self.selenium_driver)
        user_menu.selenium_driver.element_click(CommonPage.USER_DROP_DOWN)
        user_menu.selenium_driver.wait_until_element_present(user_menu.CHANGE_PASSWORD)
        user_menu.selenium_driver.element_click(user_menu.CHANGE_PASSWORD)
        self.selenium_driver.wait_until_element_present(self.CURRENT_PASSWORD)
        self.selenium_driver.wait_until_element_present(self.PASSWORD)
        self.selenium_driver.wait_until_element_present(self.CONFIRM_PASSWORD)
        self.selenium_driver.wait_until_element_present(self.CANCEL)
        self.selenium_driver.wait_until_element_present(self.SAVE)