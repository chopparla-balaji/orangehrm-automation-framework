from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class AddReports:

    REPORT_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    SELECTION_CRITERIA:Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    INCLUDE:Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    SELECT_DISPLAY_FIELD_GROUP: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[3]/ancestor::div[2]")
    SELECT_DISPLAY_FIELD: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[4]/ancestor::div[2]")

    CANCEL: Final[Locator] = (By.XPATH, "//button[@type='button']")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class Reports:

    REPORT_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    RESET: Final[Locator] = (By.XPATH, "(//button[@type='button'])[1]")
    SEARCH: Final[Locator] = (By.XPATH, "//button[@type='submit']")
    ADD_REPORTS: Final[Locator] = (By.XPATH, "(//button[@type='button'])[2]")

    DELETE_REPORT: Final[Locator] = (By.XPATH, "//div[normalize-space()='{username}']/following::button[@type='button'][1]")
    EDIT_REPORT: Final[Locator] = (By.XPATH, "//div[normalize-space()='{username}']/following::button[@type='button'][2]")
    REPORTS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[4]")

class EditReports:

    INCLUDE_HEADER: Final[Locator] = (By.XPATH, "(//input[@type='checkbox'])[1]/following::span[1]")
    DELETE_LABEL: Locator = (By.XPATH, "//span[normalize-space()='{label}']/child::i")

class ManageReports:

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver