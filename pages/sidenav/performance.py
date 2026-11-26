from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By


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