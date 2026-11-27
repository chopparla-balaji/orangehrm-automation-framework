from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

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

class Configures:

    CONFIGURE: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[5]")

    def __init__(self, selenium_driver: SeleniumDriver):
        self.selenium_driver = selenium_driver

    def wait_for_work_week_to_load(self, is_landing=True):
        if is_landing:
            self.selenium_driver.element_click(self.CONFIGURE)
            self.selenium_driver.wait_until_element_clickable(WorkWeek.WORK_WEEK)
            self.selenium_driver.element_click(WorkWeek.WORK_WEEK)
        self.selenium_driver.wait_until_element_visible(WorkWeek.SUNDAY)
        self.selenium_driver.wait_until_element_visible(WorkWeek.MONDAY)
        self.selenium_driver.wait_until_element_visible(WorkWeek.TUESDAY)
        self.selenium_driver.wait_until_element_visible(WorkWeek.WEDNESDAY)
        self.selenium_driver.wait_until_element_visible(WorkWeek.THURSDAY)
        self.selenium_driver.wait_until_element_visible(WorkWeek.FRIDAY)
        self.selenium_driver.wait_until_element_visible(WorkWeek.SATURDAY)
        self.selenium_driver.wait_until_element_visible(WorkWeek.SAVE)

    def wait_for_leave_period_to_load(self, is_landing=True):
        if is_landing:
            self.selenium_driver.element_click(self.CONFIGURE)
            self.selenium_driver.wait_until_element_clickable(LeavePeriod.LEAVE_PERIOD)
            self.selenium_driver.element_click(LeavePeriod.LEAVE_PERIOD)
        self.selenium_driver.wait_until_element_visible(LeavePeriod.START_MONTH)
        self.selenium_driver.wait_until_element_visible(LeavePeriod.START_DATE)
        self.selenium_driver.wait_until_element_visible(LeavePeriod.RESET)
        self.selenium_driver.wait_until_element_visible(LeavePeriod.SAVE)

