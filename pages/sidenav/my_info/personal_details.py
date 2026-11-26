from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class PersonalDetails:


    EMPLOYEE_FIRST_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='firstName']")
    EMPLOYEE_MIDDLE_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='middleName']")
    EMPLOYEE_LAST_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='lastName']")
    NICKNAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[4]")
    EMPLOYEE_ID: Final[Locator] = (By.XPATH, "(//form/descendant::input)[5]")
    OTHER_ID: Final[Locator] = (By.XPATH, "(//form/descendant::input)[6]")
    DRIVERS_LICENSE_NUMBER: Final[Locator] = (By.XPATH, "(//form/descendant::input)[7]")
    LICENSE_EXPIRY_DATE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[8]")
    NATIONALITY: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    MARITAL_STATUS: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[2]/ancestor::div[2]")
    DATE_OF_BIRTH: Final[Locator] = (By.XPATH, "(//form/descendant::input)[9]")
    MALE: Final[Locator] = (By.XPATH, "(//input[@type='radio'])[1]/following-sibling::span[1]")
    FEMALE: Final[Locator] = (By.XPATH, "(//input[@type='radio'])[2]/following-sibling::span[1]")
    MILITARY_SERVICE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[12]")
    SMOKER: Final[Locator] = (By.XPATH, "(//input[@type='checkbox'])[1]/following::span[1]")
    BLOOD_TYPE: Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[3]/ancestor::div[2]")
    TEST_FIELD: Final[Locator] = (By.XPATH, "(//form/descendant::input)[15]")
    SELECT_FILE: Final[Locator] = (By.XPATH, "//input[@type='file']")
    COMMENT: Final[Locator] = (By.TAG_NAME, "textarea")
    SAVE_DET: Final[Locator] = (By.XPATH, "(//button[@type='submit'])[1]")
    SAVE_FIELDS: Final[Locator] = (By.XPATH, "(//button[@type='submit'])[2]")
    CANCEL_ATTACH: Final[Locator] = (By.XPATH, "(//button[@type='button'])[1]")
    SAVE_ATTACH: Final[Locator] = (By.XPATH, "(//button[@type='submit'])[3]")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver