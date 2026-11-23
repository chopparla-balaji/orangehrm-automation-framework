from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class OptionalFields:

    SHOW_NICKNAME_SMOKER_MILITARY_SERVICE_IN_PERSONAL_DETAILS: Final[Locator] = (By.XPATH, "//label[text()='Show Nick Name, Smoker and Military Service in Personal Details']")
    SHOW_SSN_FIELD_IN_PERSONAL_DETAILS: Final[Locator] = (By.XPATH, "//label[text()='Show SSN field in Personal Details']")
    SHOW_SIN_FIELD_IN_PERSONAL_DETAILS:Final[Locator] = (By.XPATH, "//label[text()='Show SIN field in Personal Details']")
    SHOW_US_TAX_EXEMPTIONS_MENU: Final[Locator] = (By.XPATH, "//label[text()='Show US Tax Exemptions menu']")
    SAVE: Final[Locator] = (By.XPATH, "//button[normalize-space()='Save']")

class CustomFields:

    ADD_Fields: Final[Locator] = (By.XPATH, "//button[normalize-space()='Add']")
    DELETE_REPORTS: Final[Locator] = (By.XPATH, "//button[normalize-space()='Delete']")
    EDIT_REPORTS: Final[Locator] = (By.XPATH, "//button[normalize-space()='Delete']")

class EditCustomFields:

    FIELD_NAME:Final[Locator] = (By.XPATH, "//button[normalize-space()='Field Name']")
    SCREEN: Final[Locator] = (By.XPATH, "//button[normalize-space()='Screen']")
    SELECT_OPTIONS: Final[Locator] = (By.XPATH, "//button[normalize-space()='Select Options']")

    DELETE_REPORTS: Final[Locator] = (By.XPATH, "//button[normalize-space()='Delete']")
    EDIT_REPORTS: Final[Locator] = (By.XPATH, "//button[normalize-space()='Delete']")

class DataImport:

    SELECT_FILE: Final[Locator] = (By.XPATH, "//button[normalize-space()='Select File']")
    EDIT_REPORTS: Final[Locator] = (By.XPATH, "//button[normalize-space()='Delete']")
    DOWNLOAD_SAMPLE_CSV: Final[Locator] = (By.XPATH, "//button[normalize-space()='Download Sample CSV']")

class ManageConfiguration:

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver
