from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class OptionalFields:

    SHOW_NICKNAME_SMOKER_MILITARY_SERVICE_IN_PERSONAL_DETAILS: Final[Locator] = (By.XPATH, "(//input[@type='checkbox'])[1]/following::span[1]")
    SHOW_SSN_FIELD_IN_PERSONAL_DETAILS: Final[Locator] = (By.XPATH, "(//input[@type='checkbox'])[2]/following::span[1]")
    SHOW_SIN_FIELD_IN_PERSONAL_DETAILS:Final[Locator] = (By.XPATH, "(//input[@type='checkbox'])[3]/following::span[1]")
    SHOW_US_TAX_EXEMPTIONS_MENU: Final[Locator] = (By.XPATH, "(//input[@type='checkbox'])[4]/following::span[1]")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")
    OPTIONAL_FIELDS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]/"
                                          "descendant::ul[1]/descendant::li[1]")

class CustomFields:

    ADD_Fields: Final[Locator] = (By.XPATH, "//button[@type='button']")
    DELETE_CUSTOM_FIELD: Final[Locator] = (By.XPATH, "//div[normalize-space()='{field_name}']/following::button[@type='button'][1]")
    EDIT_CUSTOM_FIELD: Final[Locator] = (By.XPATH, "//div[normalize-space()='{field_name}']/following::button[@type='button'][2]")
    CUSTOM_FIELDS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]/"
                                          "descendant::ul[1]/descendant::li[2]")

class EditCustomFields:

    FIELD_NAME:Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    SCREEN: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    SELECT_OPTIONS: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")

    DELETE_FIELD: Final[Locator] = (By.XPATH, "//button[@type='button']")
    EDIT_FIELD: Final[Locator] = (By.XPATH, "//button[@type='submit']")

class DataImport:

    SELECT_FILE: Final[Locator] = (By.XPATH, "//input[@type='file']")
    UPLOAD: Final[Locator] = (By.XPATH, "//button[@type='submit']")
    DOWNLOAD_SAMPLE_CSV: Final[Locator] = (By.XPATH, "//form/preceding::a[1]")
    DATA_IMPORT: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]/"
                                          "descendant::ul[1]/descendant::li[3]")

class ManageConfiguration:

    CONFIGURATION: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[1]")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver
