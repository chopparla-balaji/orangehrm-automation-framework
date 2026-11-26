from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class JobTitles:

    JOB_TITLES: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]/"
                                          "descendant::ul[1]/descendant::li[1]")
    REC_ALL_CHX: Final[Locator] = (By.XPATH, "//div[@role='columnheader']/descendant::span[1]")
    DELETE_SELECT: Final[Locator] = (By.XPATH, "//div[@role='columnheader']/preceding::button[@type='button'][1]")
    DELETE_ACTION: Locator = (By.XPATH, "//div[normalize-space()='{job_title}']/following::button[@type='button'][1]")
    UPDATE_ACTION: Locator = (By.XPATH, "//div[normalize-space()='{job_title}']/following::button[@type='button'][2]")
    NO_CANCEL_USER: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[@type='button'][1]")
    DELETE_USER: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[@type='button'][2]")
    CLOSE_DIALOG: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[1]")
    JOB_ADD:Final[Locator] = (By.XPATH, "//button[@type='button'][1]")

    # Edit Job
    JOB_TITLE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    JOB_DESCRIPTION: Final[Locator] = (By.TAG_NAME, "textarea")
    JOB_SPECIFICATION: Final[Locator] = (By.XPATH, "//input[@type='file']")
    NOTE: Final[Locator] = (By.CSS_SELECTOR, "textarea:nth-of-type(2)")
    CANCEL: Final[Locator] = (By.XPATH, "//button[@type='button']")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class WorkShifts:

    WORK_SHITS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[2]/"
                                          "descendant::ul[1]/descendant::li[5]")
    SHIFT_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    WORK_FROM: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    WORK_TO: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    ASSIGNED_EMPLOYEE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[4]")