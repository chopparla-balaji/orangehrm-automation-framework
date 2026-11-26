from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class EmployeeList:

    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    EMPLOYEE_ID: Locator = (By.XPATH, "(//form/descendant::input)[2]")
    EMPLOYMENT_STATUS: Locator = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    INCLUDE: Locator = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    SUPERVISOR_NAME: Locator = (By.XPATH, "(//form/descendant::input)[3]")
    JOB_TITLE: Locator = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    SUB_UNIT:Locator = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    RESET: Final[Locator] = (By.XPATH, "//button[@type='reset']")
    SEARCH: Final[Locator] = (By.XPATH, "//button[@type='submit']")
    ADD_EMPLOYEE: Final[Locator] = (By.XPATH, "//button[@type='button']")
    REC_ALL_CHX: Final[Locator] = (By.XPATH, "//div[@role='columnheader']/descendant::span[1]")
    DELETE_ACTION: Locator = (By.XPATH, "//div[normalize-space()='{Id}']/following::button[@type='button'][1]")
    UPDATE_ACTION: Locator = (By.XPATH, "//div[normalize-space()='{Id}']/following::button[@type='button'][2]")
    NO_CANCEL_EMP: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[@type='button'][1]")
    DELETE_EMPLOYEE: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[@type='button'][2]")
    CLOSE_DIALOG: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[1]")
    EMPLOYEE_LIST: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]")

    # Option Value
    OPT_VAL: Locator = (By.XPATH, "//span[normalize-space()='{option}']/parent::div[@role='option']")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver