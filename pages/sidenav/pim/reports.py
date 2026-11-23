from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class AddReports:

    REPORT_NAME: Final[Locator] = (By.XPATH, "//label[normalize-space()='Report Name']/following::input[@placeholder"
                                             "='Type here ...][1]")
    SELECTION_CRITERIA:Final[Locator] = (By.XPATH, "//label[normalize-space()='Selection Criteria']/ancestor::div[2]/"
                                                   "descendant::div[2]/div[1]")
    INCLUDE:Final[Locator] = (By.XPATH, "//label[normalize-space()='Include']/ancestor::div[2]/descendant::div[2]/"
                                        "div[1]")
    SELECT_DISPLAY_FIELD_GROUP: Final[Locator] = (By.XPATH, "//label[normalize-space()='Select Display Field Group']/"
                                                            "ancestor::div[2]/descendant::div[2]/div[1]")
    SELECT_DISPLAY_FIELD: Final[Locator] = (By.XPATH, "//label[normalize-space()='Select Display Field']/ancestor::"
                                                      "div[2]/descendant::div[2]/div[1]")

    CANCEL: Final[Locator] = (By.XPATH, "//button[normalize-space()='Cancel']")
    SAVE: Final[Locator] = (By.XPATH, "//button[normalize-space()='Save']")

class Reports:

    REPORT_NAME: Final[Locator] = (By.XPATH, "//label[normalize-space()='Report Name']/following::input[@placeholder"
                                             "='Type here ...][1]")
    RESET: Final[Locator] = (By.XPATH, "//button[normalize-space()='Reset']")
    SEARCH: Final[Locator] = (By.XPATH, "//button[normalize-space()='Search']")
    ADD_REPORTS: Final[Locator] = (By.XPATH, "//button[normalize-space()='Add']")

    DELETE_REPORTS: Final[Locator] = (By.XPATH, "//button[normalize-space()='Delete']")
    EDIT_REPORTS: Final[Locator] = (By.XPATH, "//button[normalize-space()='Delete']")

class EditReports:

    INCLUDE_HEADER: Final[Locator] = (By.XPATH, "//label[normalize-space()='Include Header']/following::input[@type="
                                                "'checkbox'][1]/following-sibling::span[1]")
    DELETE_LABEL: Locator = (By.XPATH, "//span[normalize-space()='{label}']/child::i")

class ManageReports:

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver