from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class WorkWeek:

    WORK_WEEK:Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[5]/"
                                          "descendant::ul[1]/descendant::li[3]")
    MONDAY : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    TUESDAY : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    WEDNESDAY : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[3]/ancestor::div[2]")
    THURSDAY : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[4]/ancestor::div[2]")
    FRIDAY : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[5]/ancestor::div[2]")
    SATURDAY : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[6]/ancestor::div[2]")
    SUNDAY : Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[7]/ancestor::div[2]")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class LeavePeriod:

    LEAVE_PERIOD: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[5]/"
                                           "descendant::ul[1]/descendant::li[1]")
    START_MONTH: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    START_DATE: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    RESET: Final[Locator] = (By.XPATH, "//button[@type='button']")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")
