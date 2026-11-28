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
    RESET: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='reset']")
    SEARCH_CANDIDATE: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='submit']")
    ADD_CANDIDATE: Final[Locator] = (By.XPATH, "//form/following::button[@type='button']")

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
    CANCEL: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='button']")
    SAVE: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='submit']")

class ManageRecruitment:

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def wait_for_candidates_to_load(self) -> None:
        self.selenium_driver.wait_until_element_visible(Candidates.JOB_TITLE)
        self.selenium_driver.wait_until_element_visible(Candidates.VACANCY)
        self.selenium_driver.wait_until_element_visible(Candidates.HIRING_MANAGER)
        self.selenium_driver.wait_until_element_visible(Candidates.STATUS)
        self.selenium_driver.wait_until_element_present(Candidates.CANDIDATE_NAME)
        self.selenium_driver.wait_until_element_present(Candidates.KEYWORDS)
        self.selenium_driver.wait_until_element_present(Candidates.DATE_OF_APPLICATION_FROM)
        self.selenium_driver.wait_until_element_present(Candidates.DATE_OF_APPLICATION_TO)
        self.selenium_driver.wait_until_element_visible(Candidates.METHOD_OF_APPLICATION)
        self.selenium_driver.wait_until_element_present(Candidates.RESET)
        self.selenium_driver.wait_until_element_clickable(Candidates.SEARCH_CANDIDATE)
        self.selenium_driver.wait_until_element_clickable(Candidates.ADD_CANDIDATE)

    def wait_for_add_page_candidates_to_load(self, is_add: bool= True) -> None:
        if is_add:
            self.selenium_driver.window_scroll(360)
            self.selenium_driver.element_click(Candidates.ADD_CANDIDATE)
            self.selenium_driver.wait_until_element_present(AddCandidates.CANDIDATE_FIRST_NAME)
            self.selenium_driver.wait_until_element_present(AddCandidates.CANDIDATE_MIDDLE_NAME)
            self.selenium_driver.wait_until_element_present(AddCandidates.CANDIDATE_LAST_NAME)
            self.selenium_driver.wait_until_element_visible(AddCandidates.VACANCY)
            self.selenium_driver.wait_until_element_present(AddCandidates.EMAIL)
            self.selenium_driver.wait_until_element_present(AddCandidates.CONTACT_NUMBER)
            self.selenium_driver.wait_until_element_present(AddCandidates.RESUME)
            self.selenium_driver.wait_until_element_present(AddCandidates.KEYWORDS)
            self.selenium_driver.wait_until_element_present(AddCandidates.DATE_OF_APPLICATION)
            self.selenium_driver.wait_until_element_present(AddCandidates.NOTES)
            self.selenium_driver.wait_until_element_present(AddCandidates.CONSENT_TO_KEEP_DATA)
            self.selenium_driver.wait_until_element_clickable(AddCandidates.CANCEL)
            self.selenium_driver.wait_until_element_clickable(AddCandidates.SAVE)
        else:
            self.wait_for_candidates_to_load()