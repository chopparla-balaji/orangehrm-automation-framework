from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class JobTitles:

    JOB_TITLES: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]/"
                                          "descendant::ul[1]/descendant::li[1]")
    REC_ALL_CHX: Final[Locator] = (By.XPATH, "//div[@role='columnheader']/descendant::span[1]")
    DELETE_SELECT: Final[Locator] = (By.XPATH, "//div[@role='columnheader']/preceding::button[@type='button'][1]")
    JOB_ADD:Final[Locator] = (By.XPATH, "//header/following::h6/following::button[@type='button']")

    # Edit Job
    JOB_TITLE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    JOB_DESCRIPTION: Final[Locator] = (By.TAG_NAME, "textarea")
    JOB_SPECIFICATION: Final[Locator] = (By.XPATH, "//input[@type='file']")
    NOTE: Final[Locator] = (By.XPATH, "//input[@type='file']/following::textarea[1]")
    CANCEL: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='button']")
    SAVE: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='submit']")
    JOB_HEADER: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]")

class WorkShifts:

    WORK_SHIFTS_HEADER: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]"
                                                    "/descendant::ul[1]/descendant::li[5]")
    SHIFT_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    WORK_FROM: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    WORK_TO: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    ASSIGNED_EMPLOYEE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[4]")

class ManageJobs:

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def wait_for_job_titles_to_load(self, is_landing=True, is_job_add=True) -> None:
        if is_landing:
            self.selenium_driver.element_click(JobTitles.JOB_HEADER)
            self.selenium_driver.wait_until_element_visible(JobTitles.JOB_TITLES)
            self.selenium_driver.element_click(JobTitles.JOB_TITLES)
        self.selenium_driver.wait_until_element_clickable(JobTitles.JOB_ADD)
        if is_job_add:
            self.selenium_driver.element_click(JobTitles.JOB_ADD)
            self.selenium_driver.wait_until_element_present(JobTitles.JOB_TITLE)
            self.selenium_driver.wait_until_element_present(JobTitles.JOB_DESCRIPTION)
            self.selenium_driver.wait_until_element_present(JobTitles.JOB_SPECIFICATION)
            self.selenium_driver.wait_until_element_present(JobTitles.NOTE)
            self.selenium_driver.wait_until_element_clickable(JobTitles.CANCEL)
            self.selenium_driver.wait_until_element_clickable(JobTitles.SAVE)

    def wait_for_job_work_shifts_to_load(self, is_landing:bool=True, is_shift_add:bool=True) -> None:
        if is_landing:
            self.selenium_driver.element_click(JobTitles.JOB_HEADER)
            self.selenium_driver.wait_until_element_visible(WorkShifts.WORK_SHIFTS_HEADER)
            self.selenium_driver.element_click(WorkShifts.WORK_SHIFTS_HEADER)
        self.selenium_driver.wait_until_element_present(JobTitles.JOB_ADD)
        if is_shift_add:
            self.selenium_driver.element_click(JobTitles.JOB_ADD)
            self.selenium_driver.wait_until_element_present(WorkShifts.SHIFT_NAME)
            self.selenium_driver.wait_until_element_present(WorkShifts.WORK_FROM)
            self.selenium_driver.wait_until_element_present(WorkShifts.WORK_TO)
            self.selenium_driver.wait_until_element_present(WorkShifts.ASSIGNED_EMPLOYEE)
            self.selenium_driver.wait_until_element_clickable(JobTitles.CANCEL)
            self.selenium_driver.wait_until_element_clickable(JobTitles.SAVE)