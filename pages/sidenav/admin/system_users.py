from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.sidenav.sidenav import SideNav
from utils.utils import format_locator_text
from utils.constants import USER_NAME, ROLE, NAME, STATUS, EMPTY_SEARCH_RESULT


class SystemUsers:

    USERNAME: Final[Locator] = (By.XPATH, "//form/descendant::input[1]")
    USER_ROLE: Final[Locator] = (By.XPATH, "//div[@tabIndex='0']/ancestor::div[2]")
    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "//form/descendant::input[2]")
    STATUS: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    RESET: Final[Locator] = (By.XPATH, "//button[@type='button']")
    SEARCH: Final[Locator] = (By.XPATH, "//button[@type='submit']")
    ADD_USER: Final[Locator] = (By.XPATH, "(//button[@type='button'])[2]")
    REC_ALL_CHX: Final[Locator] = (By.XPATH, "//div[@role='columnheader']/descendant::span[1]")
    DELETE_SELECT: Final[Locator] = (By.XPATH, "//div[@role='columnheader']/preceding::button[@type='button'][1]")
    DELETE_ACTION: Locator = (By.XPATH, "//div[normalize-space()='{username}']/following::button[@type='button'][1]")
    UPDATE_ACTION: Locator = (By.XPATH, "//div[normalize-space()='{username}']/following::button[@type='button'][2]")
    NO_CANCEL_USER: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[@type='button'][1]")
    DELETE_USER: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[@type='button'][2]")
    CLOSE_DIALOG: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[1]")
    ROW_GROUP: Final[Locator] = (By.XPATH, "(//div[@role='rowgroup'])[2]")

    # Option Value
    OPT_VAL: Locator = (By.XPATH, "//*[normalize-space()='{option}']/parent::div[@role='option']")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def landing_user_management(self) -> None:
        self.selenium_driver.wait_until_element_present(SideNav.ADMIN)
        self.selenium_driver.wait_until_element_present(SideNav.DASHBOARD)
        self.selenium_driver.element_click(SideNav.ADMIN)
        self.validate_system_user()

    def validate_system_user(self) -> None:
        self.selenium_driver.wait_until_element_present(self.USERNAME)
        self.selenium_driver.wait_until_element_present(self.USER_ROLE)
        self.selenium_driver.wait_until_element_present(self.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(self.STATUS)
        self.selenium_driver.wait_until_element_present(self.RESET)
        self.selenium_driver.wait_until_element_present(self.SEARCH)
        self.selenium_driver.validate_page_title()

    def wait_delete_confirmation_dialog(self, is_open: bool=True) -> None:
        if is_open:
            self.selenium_driver.wait_until_element_visible(self.CLOSE_DIALOG)
            self.selenium_driver.wait_until_element_visible(self.NO_CANCEL_USER)
            self.selenium_driver.wait_until_element_visible(self.DELETE_USER)
        else:
            self.selenium_driver.wait_until_element_in_visible(self.CLOSE_DIALOG)
            self.selenium_driver.wait_until_element_in_visible(self.NO_CANCEL_USER)
            self.selenium_driver.wait_until_element_in_visible(self.DELETE_USER)

    def search_user(self, user_information: dict[str, str]) -> None:
        if USER_NAME in user_information:
            self.selenium_driver.send_keys(self.USERNAME, user_information[USER_NAME])
        if ROLE in user_information:
            self.selenium_driver.element_click(self.USER_ROLE)
            self.selenium_driver.select_option_element(self.OPT_VAL, user_information[ROLE])
        if NAME in user_information:
            self.selenium_driver.send_keys(self.EMPLOYEE_NAME, user_information[NAME])
            self.selenium_driver.select_option_element(self.OPT_VAL, user_information[NAME], 40)
        if STATUS in user_information:
            self.selenium_driver.element_click(self.STATUS)
            self.selenium_driver.select_option_element(self.OPT_VAL, user_information[STATUS], 40)
        self.selenium_driver.element_click(self.SEARCH)
        text = self.selenium_driver.get_text(self.ROW_GROUP)
        if not text:
            print(EMPTY_SEARCH_RESULT)