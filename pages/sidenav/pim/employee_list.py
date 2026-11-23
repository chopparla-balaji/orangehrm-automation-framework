from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class EmployeeList:

    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "//label[normalize-space()='Employee Name']/following::input"
                                               "[@placeholder='Type for hints...'][1]")
    EMPLOYEE_ID: Locator = (By.XPATH, "//label[normalize-space()='Employee Id']/following::input[1]/ancestor::div[2]"
                                      "/descendant::div[2]/div[1]")
    EMPLOYMENT_STATUS: Locator = (By.XPATH, "//label[normalize-space()='Employment Status']")
    INCLUDE: Locator = (By.XPATH, "//label[normalize-space()='Include']/ancestor::div[2]/descendant::div[2]/div[1]")
    SUPERVISOR_NAME: Locator = (By.XPATH, "//label[normalize-space()='Supervisor Name']/following::input"
                                               "[@placeholder='Type for hints...'][1]")
    JOB_TITLE: Locator = (By.XPATH, "//label[normalize-space()='Job Title']/ancestor::div[2]/descendant::div[2]/div[1]")
    SUB_UNIT:Locator = (By.XPATH, "//label[normalize-space()='Sub Unit']/ancestor::div[2]/descendant::div[2]/div[1]")
    RESET: Final[Locator] = (By.XPATH, "//button[normalize-space()='Reset']")
    SEARCH: Final[Locator] = (By.XPATH, "//button[normalize-space()='Search']")
    ADD_USER: Final[Locator] = (By.XPATH, "//button[normalize-space()='Add']")
    REC_ALL_CHX: Final[Locator] = (By.XPATH, "//div[@role='columnheader' and normalize-space()='Id']/preceding"
                                             "::input[@type='checkbox'][1]")
    DELETE_ACTION: Locator = (By.XPATH, "//div[normalize-space()='{Id}']/following::button[@type='button'][1]")
    UPDATE_ACTION: Locator = (By.XPATH, "//div[normalize-space()='{Id}']/following::button[@type='button'][2]")
    NO_CANCEL_USER: Final[Locator] = (By.XPATH, "//button[normalize-space()='No, Cancel']")
    DELETE_USER: Final[Locator] = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
    CLOSE_DIALOG: Final[Locator] = (By.XPATH, "//button[normalize-space()='×']")

    # Option Value
    OPT_VAL: Locator = (By.XPATH, "//span[normalize-space()='{option}']/parent::div[@role='option']")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver