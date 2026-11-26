from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class AssignLeave:

    APPLY_LEAVE: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[7]")
    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    LEAVE_TYPE: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    FROM_DATE : Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    TO_DATE : Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    COMMENTS : Final[Locator] = (By.TAG_NAME, "textarea")
    ASSIGN: Final[Locator] = (By.XPATH, "//button[@type='submit']")