from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class EmployeeAttendanceRec:

    RECORDS : Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]/"
                                          "descendant::ul[1]/descendant::li[3]")
    EMPLOYEE_NAME : Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    ATTENDANCE : Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]")
    DATE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    VIEW: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class EmployeeReports:

    EMPLOYEE_REPORTS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]/"
                                          "descendant::ul[1]/descendant::li[2]")
    REPORTS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]")
    PROJECT_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    ACTIVITY_NAME: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    PROJECT_DATE_RANGE_FROM: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    PROJECT_DATE_RANGE_TO: Final[Locator] = (By.XPATH, "(//form/descendant::input)[4]")
    ONLY_INCLUDE_APPROVED_TIMESHEETS: Final[Locator] = (By.XPATH, "//input[@type='checkbox']/following::span[1]")
    VIEW: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class Customers:

    PROJECT_INFO: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[4]")
    CUSTOMERS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[4]/"
                                          "descendant::ul[1]/descendant::li[1]")
    ADD: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class AddCustomers:

    NAME: Final[Locator] = (By.TAG_NAME, "input")
    DESCRIPTION: Final[Locator] = (By.TAG_NAME, "textarea")
    CANCEL: Final[Locator] = (By.XPATH, "(//button[@type='submit'])[1]")
    SAVE: Final[Locator] = (By.XPATH, "(//button[@type='submit'])[2]")

class ManageTime:

    def __init__(self, selenium_driver: SeleniumDriver):
        self.selenium_driver = selenium_driver

    def wait_for_time_sheet_to_load(self):
        self.selenium_driver.wait_until_element_present(EmployeeAttendanceRec.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(EmployeeAttendanceRec.VIEW)

    def wait_for_employee_attendance_rec_to_load(self, is_landing=True):
        if is_landing:
            self.selenium_driver.element_click(EmployeeAttendanceRec.ATTENDANCE)
            self.selenium_driver.wait_until_element_visible(EmployeeAttendanceRec.RECORDS)
            self.selenium_driver.element_click(EmployeeAttendanceRec.RECORDS)
        self.selenium_driver.wait_until_element_present(EmployeeAttendanceRec.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(EmployeeAttendanceRec.DATE)
        self.selenium_driver.wait_until_element_present(EmployeeAttendanceRec.VIEW)

    def wait_for_employee_reports_to_load(self, is_landing=True):
        if is_landing:
            self.selenium_driver.element_click(EmployeeReports.REPORTS)
            self.selenium_driver.wait_until_element_visible(EmployeeReports.EMPLOYEE_REPORTS)
            self.selenium_driver.element_click(EmployeeReports.EMPLOYEE_REPORTS)
        self.selenium_driver.wait_until_element_present(EmployeeAttendanceRec.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(EmployeeReports.PROJECT_NAME)
        self.selenium_driver.wait_until_element_present(EmployeeReports.ACTIVITY_NAME)
        self.selenium_driver.wait_until_element_present(EmployeeReports.PROJECT_DATE_RANGE_FROM)
        self.selenium_driver.wait_until_element_present(EmployeeReports.PROJECT_DATE_RANGE_TO)
        self.selenium_driver.wait_until_element_present(EmployeeReports.VIEW)

    def wait_for_customers_to_load(self, is_landing=True, is_add_customer=False):
        if is_landing:
            self.selenium_driver.element_click(Customers.PROJECT_INFO)
            self.selenium_driver.wait_until_element_visible(Customers.CUSTOMERS)
            self.selenium_driver.element_click(Customers.CUSTOMERS)
        if is_add_customer:
            self.selenium_driver.wait_until_element_present(AddCustomers.NAME)
            self.selenium_driver.wait_until_element_present(AddCustomers.DESCRIPTION)
            self.selenium_driver.wait_until_element_present(AddCustomers.CANCEL)
            self.selenium_driver.wait_until_element_present(AddCustomers.SAVE)
        else:
            self.selenium_driver.wait_until_element_present(Customers.ADD)
