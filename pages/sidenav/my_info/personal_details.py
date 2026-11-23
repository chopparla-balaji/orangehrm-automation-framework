from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class PersonalDetails:


    EMPLOYEE_FIRST_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='firstName'][placeholder='First Name']")
    EMPLOYEE_MIDDLE_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='middleName'][placeholder='Middle Name']")
    EMPLOYEE_LAST_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='lastName'][placeholder='Last Name']")
    EMPLOYEE_ID: Final[Locator] = (By.XPATH, "//Employee Id")
    OTHER_ID: Final[Locator] = (By.XPATH, "//Other Id")
    DRIVERS_LICENSE_NUMBER: Final[Locator] = (By.XPATH, "//Driver's License Number")
    LICENSE_EXPIRY_DATE: Final[Locator] = (By.XPATH, "//License Expiry Date")
    NATIONALITY: Final[Locator] = (By.XPATH, "//Nationality")
    MARITAL_STATUS: Final[Locator] = (By.XPATH, "//Marital Status")
    DATE_OF_BIRTH: Final[Locator] = (By.XPATH, "//Date of Birth")
    MALE: Final[Locator] = (By.XPATH, "//Male")
    FEMALE: Final[Locator] = (By.XPATH, "//Fe Male")
    BLOOD_TYPE: Final[Locator] = (By.XPATH, "//Blood Type")
    TEST_FIELD: Final[Locator] = (By.XPATH, "//Test_Field")
    SELECT_FILE: Final[Locator] = (By.XPATH, "//Select File")
    COMMENT: Final[Locator] = (By.XPATH, "//Comment")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver