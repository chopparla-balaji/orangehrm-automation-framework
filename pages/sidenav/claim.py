from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class AssignClaim:

    EMPLOYEE_NAME : Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    EVENT : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    CURRENCY : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    REMARKS:Final[Locator] = (By.TAG_NAME, "textarea")
    ASSIGN_CLAIM_HEADER:Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[5]")
    CANCEL: Final[Locator] = (By.XPATH, "//button[@type='button']")
    CREATE: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class MyClaims:

    REFERENCE_ID : Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    EVENT_NAME : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    STATUS : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    FROM_DATE : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[3]/ancestor::div[2]")
    TO_DATE : Final[Locator] = (By.LINK_TEXT, "(//div[@tabIndex='0'])[4]/ancestor::div[2]")
    RESET: Final[Locator] = (By.XPATH, "//button[@type='button']")
    SEARCH: Final[Locator] = (By.XPATH, "//button[@type='submit']")
    MY_CLAIMS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]")

class EmployeeClaims:

    EVENT_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    STATUS: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    ASSIGN_CLAIM: Final[Locator] = (By.XPATH, "(//button[@type='button'])[2]")