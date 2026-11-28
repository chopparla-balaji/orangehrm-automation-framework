from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class EmployeeList:

    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    EMPLOYEE_ID: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    EMPLOYMENT_STATUS: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    INCLUDE: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    SUPERVISOR_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    JOB_TITLE: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[3]/ancestor::div[2]")
    SUB_UNIT:Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[4]/ancestor::div[2]")
    RESET: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='reset']")
    SEARCH_EMP_LIST: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='submit']")
    ADD_EMPLOYEE: Final[Locator] = (By.XPATH, "//form/following::button[@type='button']")
    REC_ALL_CHX: Final[Locator] = (By.XPATH, "//div[@role='columnheader']/descendant::span[1]")
    EMPLOYEE_LIST: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]")

    # Option Value
    OPT_VAL: Locator = (By.XPATH, "//span[normalize-space()='{option}']/parent::div[@role='option']")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def wait_for_employee_list_to_load(self, is_landing:bool = True) -> None:
        if is_landing:
            self.selenium_driver.element_click(self.EMPLOYEE_LIST)
        self.selenium_driver.wait_until_element_present(self.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(self.EMPLOYEE_ID)
        self.selenium_driver.wait_until_element_visible(self.EMPLOYMENT_STATUS)
        self.selenium_driver.wait_until_element_visible(self.INCLUDE)
        self.selenium_driver.wait_until_element_present(self.SUPERVISOR_NAME)
        self.selenium_driver.wait_until_element_visible(self.JOB_TITLE)
        self.selenium_driver.wait_until_element_visible(self.SUB_UNIT)
        self.selenium_driver.wait_until_element_clickable(self.RESET)
        self.selenium_driver.wait_until_element_clickable(self.SEARCH_EMP_LIST)
