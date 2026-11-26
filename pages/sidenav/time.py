from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class EmployeeAttendance:

    RECORDS : Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]/"
                                          "descendant::ul[1]/descendant::li[3]")
    EMPLOYEE_NAME : Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    ATTENDANCE : Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]")
    DATE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    VIEW: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class EmployeeReports:

    EMPLOYEE_REPORTS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]/"
                                          "descendant::ul[1]/descendant::li[3]")
    REPORTS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]")
    PROJECT_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    ACTIVITY_NAME: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    PROJECT_DATE_RANGE_FROM: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    PROJECT_DATE_RANGE_TO: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    ONLY_INCLUDE_APPROVED_TIMESHEETS: Final[Locator] = (By.XPATH, "//input[@type='checkbox']/following::span[1]")
    VIEW: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class CUSTOMERS:

    PROJECT_INFO: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[4]")
    CUSTOMERS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[4]/"
                                          "descendant::ul[1]/descendant::li[1]")
    ADD: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class AddCustomers:

    NAME: Final[Locator] = (By.TAG_NAME, "input")
    DESCRIPTION: Final[Locator] = (By.TAG_NAME, "textarea")
    CANCEL: Final[Locator] = (By.XPATH, "(//button[@type='submit'])[1]")
    SAVE: Final[Locator] = (By.XPATH, "(//button[@type='submit'])[2]")