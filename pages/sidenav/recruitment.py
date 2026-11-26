from typing import Final
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from utils.type_checker import Locator

class Candidates:

    JOB_TITLE: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    VACANCY: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    HIRING_MANAGER: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[3]/ancestor::div[2]")
    STATUS: Final[Locator] = (By.XPATH, "//div[@tabIndex='0']/ancestor::div[4]")
    CANDIDATE_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    KEYWORDS: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    DATE_OF_APPLICATION_FROM: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    DATE_OF_APPLICATION_TO: Final[Locator] = (By.XPATH, "(//form/descendant::input)[4]")
    METHOD_OF_APPLICATION: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[5]/ancestor::div[2]")
    RESET: Final[Locator] = (By.XPATH, "//button[@type='reset']")
    SEARCH: Final[Locator] = (By.XPATH, "//button[@type='submit']")
    ADD: Final[Locator] = (By.XPATH, "//button[@type='button']")

class AddCandidates:

    CANDIDATE_FIRST_NAME: Final[Locator] = (By.NAME, "firstName")
    CANDIDATE_MIDDLE_NAME: Final[Locator] = (By.NAME, "middleName")
    CANDIDATE_LAST_NAME: Final[Locator] = (By.NAME, "lastName")
    VACANCY: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    EMAIL: Final[Locator] = (By.XPATH, "(//form/descendant::input)[4]")
    CONTACT_NUMBER: Final[Locator] = (By.XPATH, "(//form/descendant::input)[5]")
    RESUME: Final[Locator] = (By.CSS_SELECTOR, "input[type='file']")
    KEYWORDS: Final[Locator] = (By.XPATH, "(//form/descendant::input)[7]")
    DATE_OF_APPLICATION: Final[Locator] = (By.XPATH, "(//form/descendant::input)[8]")
    NOTES: Final[Locator] = (By.TAG_NAME, "textarea")
    CONSENT_TO_KEEP_DATA: Final[Locator] = (By.XPATH, "//input[@type='checkbox']/following::span[1]")
    CANCEL: Final[Locator] = (By.XPATH, "(//button[@type='button'])[1]")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")