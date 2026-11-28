from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class AssignClaim:

    EMPLOYEE_NAME : Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    EVENT : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    CURRENCY : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    REMARKS:Final[Locator] = (By.TAG_NAME, "textarea")
    ASSIGN_CLAIM_HEADER:Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[5]")
    CANCEL: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='button']")
    CREATE_CLAIM: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='submit']")

class MyClaims:

    REFERENCE_ID : Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    EVENT_NAME : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    STATUS : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    FROM_DATE : Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    TO_DATE : Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    RESET: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='button']")
    SEARCH_CLAIMS: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='submit']")
    MY_CLAIMS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]")

class EmployeeClaims:

    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    REFERENCE_ID: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    STATUS: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    ASSIGN_CLAIM: Final[Locator] = (By.XPATH, "//form/following::button[@type='button']")
    FROM_DATE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    TO_DATE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[4]")

class ManageClaims:

    def __init__(self, selenium_driver: SeleniumDriver):
        self.selenium_driver = selenium_driver

    def wait_for_employee_claims_to_load(self):
        self.selenium_driver.wait_until_element_present(EmployeeClaims.EMPLOYEE_NAME)
        self.selenium_driver.wait_until_element_present(EmployeeClaims.REFERENCE_ID)
        self.selenium_driver.wait_until_element_visible(MyClaims.EVENT_NAME)
        self.selenium_driver.wait_until_element_visible(MyClaims.STATUS)
        self.selenium_driver.wait_until_element_present(EmployeeClaims.FROM_DATE)
        self.selenium_driver.wait_until_element_present(EmployeeClaims.TO_DATE)
        self.selenium_driver.wait_until_element_clickable(MyClaims.RESET)
        self.selenium_driver.wait_until_element_clickable(MyClaims.SEARCH_CLAIMS)

    def wait_for_assign_claims_to_load(self, is_assign_claim=True):
        if is_assign_claim:
            self.selenium_driver.element_click(AssignClaim.ASSIGN_CLAIM_HEADER)
        self.selenium_driver.wait_until_element_visible(AssignClaim.EVENT)
        self.selenium_driver.wait_until_element_visible(AssignClaim.CURRENCY)
        self.selenium_driver.wait_until_element_present(AssignClaim.REMARKS)
        self.selenium_driver.wait_until_element_clickable(AssignClaim.CANCEL)
        self.selenium_driver.wait_until_element_clickable(AssignClaim.CREATE_CLAIM)

    def wait_for_my_claims_to_load(self, is_my_claim=True):
        if is_my_claim:
            self.selenium_driver.element_click(MyClaims.MY_CLAIMS)
        self.selenium_driver.wait_until_element_present(MyClaims.REFERENCE_ID)
        self.selenium_driver.wait_until_element_visible(MyClaims.EVENT_NAME)
        self.selenium_driver.wait_until_element_visible(MyClaims.STATUS)
        self.selenium_driver.wait_until_element_present(MyClaims.FROM_DATE)
        self.selenium_driver.wait_until_element_present(MyClaims.TO_DATE)
        self.selenium_driver.wait_until_element_clickable(MyClaims.RESET)
        self.selenium_driver.wait_until_element_clickable(MyClaims.SEARCH_CLAIMS)