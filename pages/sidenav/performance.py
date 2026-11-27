from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class EmployeeTrackers:

    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    INCLUDE:Final[Locator] = (By.XPATH, "//div[@tabIndex='0']/ancestor::div[2]")
    EMPLOYEE_TRACKER: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[4]")
    RESET: Final[Locator] = (By.XPATH, "//button[@type='reset']")
    SEARCH: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class EmployeeReviews:

    MANAGE_REVIEWS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]")
    EMPLOYEE_REVIEWS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]/"
                                          "descendant::ul[1]/descendant::li[3]")
    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    JOB_TITLE:Final[Locator] = (By.XPATH, "//div[@tabIndex='0']/ancestor::div[2]")
    SUB_UNIT:Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    INCLUDE: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[3]/ancestor::div[2]")
    REVIEW_STATUS:Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[4]/ancestor::div[2]")
    FROM_DATE:Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    TO_DATE:Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    RESET: Final[Locator] = (By.XPATH, "//button[@type='reset']")
    SEARCH: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class EmployeePerformance:

    def __init__(self, selenium_driver: SeleniumDriver):
        self.selenium_driver = selenium_driver

    def wait_for_employee_reviewers_to_load(self, is_landing_page: bool=True):
        if is_landing_page:
            self.selenium_driver.element_click(EmployeeReviews.MANAGE_REVIEWS)
            self.selenium_driver.wait_until_element_visible(EmployeeReviews.EMPLOYEE_REVIEWS)
            self.selenium_driver.element_click(EmployeeReviews.EMPLOYEE_REVIEWS)
        self.selenium_driver.wait_until_element_present(EmployeeReviews.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(EmployeeReviews.JOB_TITLE)
        self.selenium_driver.wait_until_element_present(EmployeeReviews.SUB_UNIT)
        self.selenium_driver.wait_until_element_present(EmployeeReviews.INCLUDE)
        self.selenium_driver.wait_until_element_present(EmployeeReviews.REVIEW_STATUS)
        self.selenium_driver.wait_until_element_present(EmployeeReviews.FROM_DATE)
        self.selenium_driver.wait_until_element_present(EmployeeReviews.TO_DATE)
        self.selenium_driver.wait_until_element_present(EmployeeReviews.RESET)
        self.selenium_driver.wait_until_element_present(EmployeeReviews.SEARCH)

    def wait_for_employee_trackers_to_load(self, is_landing_page: bool=True):
        if is_landing_page:
            self.selenium_driver.element_click(EmployeeTrackers.EMPLOYEE_TRACKER)
        self.selenium_driver.wait_until_element_present(EmployeeTrackers.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(EmployeeTrackers.INCLUDE)
        self.selenium_driver.wait_until_element_present(EmployeeTrackers.RESET)
        self.selenium_driver.wait_until_element_present(EmployeeTrackers.SEARCH)