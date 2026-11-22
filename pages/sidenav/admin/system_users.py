from typing import Final
from utils.type_checker import Locator
from utils.page_titles import PAGE_TITLE
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.sidenav.sidenav import SideNav
from utils.constants import USER_NAME, ROLE, NAME, STATUS

class SystemUsers:

    SYSTEM_USERS_HEADING: Final[Locator] = (By.XPATH, "//h5[normalize-space()='System Users']")
    USERNAME: Final[Locator] = (By.XPATH, "//label[text()='Username']/ancestor::div[2]/descendant::input[1]")
    USER_ROLE: Final[Locator] = (By.XPATH, "//label[text()='User Role']/ancestor::div[2]/descendant::div[2]/div[1]")
    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "//label[text()='Employee Name']/following::input[@placeholder='Type "
                                               "for hints...'][1]")
    STATUS: Final[Locator] = (By.XPATH, "//label[text()='Status']/ancestor::div[2]/descendant::div[2]/div[1]")
    RESET: Final[Locator] = (By.XPATH, "//button[normalize-space()='Reset']")
    SEARCH: Final[Locator] = (By.XPATH, "//button[normalize-space()='Search']")
    ADD_USER: Final[Locator] = (By.XPATH, "//button[normalize-space()='Add']")
    REC_ALL_CHX: Final[Locator] = (By.XPATH, "//div[@role='columnheader' and normalize-space()='Username']/preceding"
                                             "::input[@type='checkbox'][1]")
    DELETE_SELECT:Final[Locator] = (By.XPATH, "//button[contains(text(),'Delete Selected')]")
    DELETE_ACTION:Final[Locator] = (By.XPATH, "//div[normalize-space()='{username}']/following::button[@type='button'][1]")
    UPDATE_ACTION:Final[Locator] = (By.XPATH, "//div[normalize-space()='{username}']/following::button[@type='button'][2]")
    NO_CANCEL_USER: Final[Locator] = (By.XPATH, "//button[normalize-space()='No, Cancel']")
    DELETE_USER: Final[Locator] = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
    CLOSE_DIALOG:Final[Locator] = (By.XPATH, "//button[normalize-space()='×']")

    # Option Value
    OPT_VAL:Final[Locator] = (By.XPATH, "//span[normalize-space()='{option}']/parent::div[@role='option']")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def landing_user_management(self) -> None:
        self.selenium_driver.wait_until_element_present(SideNav.ADMIN)
        self.selenium_driver.wait_until_element_present(SideNav.DASHBOARD)
        self.selenium_driver.element_click(SideNav.ADMIN)
        self.validate_system_user()

    def validate_system_user(self) -> None:
        self.selenium_driver.wait_until_element_present(self.SYSTEM_USERS_HEADING)
        self.selenium_driver.wait_until_element_present(self.USERNAME)
        self.selenium_driver.wait_until_element_present(self.USER_ROLE)
        self.selenium_driver.wait_until_element_present(self.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(self.STATUS)
        self.selenium_driver.wait_until_element_present(self.RESET)
        self.selenium_driver.wait_until_element_present(self.SEARCH)
        self.selenium_driver.validate_page_title(PAGE_TITLE)

    def search_user(self, user_information:dict[str, str]) -> None:
        # user information contains [username, role, name, status] [Give Dict keys]
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

