from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LeaveList:

    FROM_DATE : Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    TO_DATE : Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    SHOW_LEAVE_WITH_STATUS : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    LEAVE_TYPE : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    SEARCH: Final[Locator] = (By.XPATH, "//button[@type='submit']")


class AssignLeave:

    ASSIGN_LEAVE: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[7]")
    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    LEAVE_TYPE: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    FROM_DATE : Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    TO_DATE : Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    COMMENTS : Final[Locator] = (By.TAG_NAME, "textarea")
    ASSIGN: Final[Locator] = (By.XPATH, "//button[@type='submit']")

    def __init__(self, selenium_driver: SeleniumDriver):
        self.selenium_driver = selenium_driver

    def wait_for_assign_leave_to_load(self, is_landing=True):
        if is_landing:
            self.selenium_driver.element_click(self.ASSIGN_LEAVE)
        self.selenium_driver.wait_until_element_present(self.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(self.LEAVE_TYPE)
        self.selenium_driver.wait_until_element_present(self.FROM_DATE)
        self.selenium_driver.wait_until_element_present(self.TO_DATE)
        self.selenium_driver.wait_until_element_present(self.COMMENTS)
        self.selenium_driver.wait_until_element_present(self.ASSIGN)

    def wait_for_leave_list_to_load(self):
        self.selenium_driver.wait_until_element_present(LeaveList.FROM_DATE)
        self.selenium_driver.wait_until_element_present(LeaveList.TO_DATE)
        self.selenium_driver.wait_until_element_present(LeaveList.SHOW_LEAVE_WITH_STATUS)
        self.selenium_driver.wait_until_element_present(LeaveList.LEAVE_TYPE)
        self.selenium_driver.wait_until_element_present(LeaveList.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(LeaveList.SEARCH)
