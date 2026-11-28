from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class OptionalFields:

    SHOW_NICKNAME_SMOKER_MILITARY_SERVICE_IN_PERSONAL_DETAILS: Final[Locator] = (By.XPATH, "(//input[@type='checkbox'])[1]/following::span[1]")
    SHOW_SSN_FIELD_IN_PERSONAL_DETAILS: Final[Locator] = (By.XPATH, "(//input[@type='checkbox'])[2]/following::span[1]")
    SHOW_SIN_FIELD_IN_PERSONAL_DETAILS:Final[Locator] = (By.XPATH, "(//input[@type='checkbox'])[3]/following::span[1]")
    SHOW_US_TAX_EXEMPTIONS_MENU: Final[Locator] = (By.XPATH, "(//input[@type='checkbox'])[4]/following::span[1]")
    SAVE: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='submit']")
    OPTIONAL_FIELDS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[1]/"
                                          "descendant::ul[1]/descendant::li[1]")

class CustomFields:

    ADD_FIELDS: Final[Locator] = (By.XPATH, "//header/following::h6/following::button[@type='button']")
    CUSTOM_FIELDS: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[1]/"
                                          "descendant::ul[1]/descendant::li[2]")

class AddCustomFields:

    FIELD_NAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    SCREEN: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    TYPE: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")

    CANCEL: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='button']")
    SUBMIT: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='submit']")

class EditCustomFields:

    FIELD_NAME:Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    SCREEN: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    SELECT_OPTIONS: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")

class DataImport:

    SELECT_FILE: Final[Locator] = (By.XPATH, "//form/descendant::input[@type='file']")
    UPLOAD: Final[Locator] = (By.XPATH, "//form/descendant::button[@type='submit']")
    DOWNLOAD_SAMPLE_CSV: Final[Locator] = (By.XPATH, "//form/preceding::a[1]")
    DATA_IMPORT: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[1]/"
                                          "descendant::ul[1]/descendant::li[3]")

class ManageConfiguration:

    CONFIGURATION: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[1]")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def wait_for_optional_fields_to_load(self, is_landing=True) -> None:
        if is_landing:
            self.selenium_driver.element_click(self.CONFIGURATION)
            self.selenium_driver.wait_until_element_visible(OptionalFields.OPTIONAL_FIELDS)
            self.selenium_driver.element_click(OptionalFields.OPTIONAL_FIELDS)
        self.selenium_driver.wait_until_element_visible(OptionalFields.SHOW_NICKNAME_SMOKER_MILITARY_SERVICE_IN_PERSONAL_DETAILS)
        self.selenium_driver.wait_until_element_visible(OptionalFields.SHOW_SSN_FIELD_IN_PERSONAL_DETAILS)
        self.selenium_driver.wait_until_element_visible(OptionalFields.SHOW_SIN_FIELD_IN_PERSONAL_DETAILS)
        self.selenium_driver.wait_until_element_visible(OptionalFields.SHOW_US_TAX_EXEMPTIONS_MENU)
        self.selenium_driver.wait_until_element_clickable(OptionalFields.SAVE)

    def wait_for_custom_fields_to_load(self, is_landing=True) -> None:
        if is_landing:
            self.selenium_driver.element_click(self.CONFIGURATION)
            self.selenium_driver.wait_until_element_present(CustomFields.CUSTOM_FIELDS)
            self.selenium_driver.element_click(CustomFields.CUSTOM_FIELDS)
        self.selenium_driver.wait_until_element_clickable(CustomFields.ADD_FIELDS)

    def wait_for_add_custom_fields_to_load(self, is_add=True) -> None:
        if is_add:
            self.selenium_driver.element_click(CustomFields.ADD_FIELDS)
        self.selenium_driver.wait_until_element_present(AddCustomFields.FIELD_NAME)
        self.selenium_driver.wait_until_element_visible(AddCustomFields.TYPE)
        self.selenium_driver.wait_until_element_visible(AddCustomFields.SCREEN)
        self.selenium_driver.wait_until_element_clickable(AddCustomFields.SUBMIT)
        self.selenium_driver.wait_until_element_clickable(AddCustomFields.CANCEL)

    def wait_for_edit_custom_fields_to_save(self, custom_field='') -> None:
        if custom_field:
            self.selenium_driver.element_click(CustomFields.CUSTOM_FIELDS)
            self.selenium_driver.wait_until_element_present(EditCustomFields.FIELD_NAME)
            self.selenium_driver.wait_until_element_visible(EditCustomFields.SCREEN)
            self.selenium_driver.wait_until_element_present(EditCustomFields.SELECT_OPTIONS)
            self.selenium_driver.wait_until_element_clickable(AddCustomFields.CANCEL)
            self.selenium_driver.wait_until_element_clickable(AddCustomFields.SUBMIT)

    def wait_for_data_import_to_load(self, is_landing=True) -> None:
        if is_landing:
            self.selenium_driver.element_click(self.CONFIGURATION)
            self.selenium_driver.wait_until_element_visible(DataImport.DATA_IMPORT)
            self.selenium_driver.element_click(DataImport.DATA_IMPORT)
        self.selenium_driver.wait_until_element_present(DataImport.SELECT_FILE)
        self.selenium_driver.wait_until_element_present(DataImport.DOWNLOAD_SAMPLE_CSV)
        self.selenium_driver.wait_until_element_clickable(DataImport.UPLOAD)