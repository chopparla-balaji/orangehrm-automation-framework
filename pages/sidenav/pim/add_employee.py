from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class AddEmployee:

    ADD_EMPLOYEE_PIC: Final[Locator] = (By.CSS_SELECTOR, "input[type='file']")
    EMPLOYEE_FIRST_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='firstName'][placeholder='First Name']")
    EMPLOYEE_MIDDLE_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='middleName'][placeholder='Middle Name']")
    EMPLOYEE_LAST_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='lastName'][placeholder='Last Name']")
    EMPLOYEE_ID: Final[Locator] = (By.XPATH, "//label[normalize-space()='Employee Id']/following::input")
    CREATE_LOGIN_DETAILS: Final[Locator] = (By.XPATH, "//label[normalize-space()='Create Login Details']/following::"
                                                      "input[@type='checkbox'][1]/span[1]")
    CANCEL: Final[Locator] = (By.XPATH, "//button[normalize-space()='Cancel']")
    SAVE: Final[Locator] = (By.XPATH, "//button[normalize-space()='Search']")
    USERNAME: Final[Locator] = (By.XPATH, "//label[normalize-space()='Username']/following::input[1]")
    ENABLED: Final[Locator] = (By.XPATH, "//label[normalize-space()='Enabled']/following-sibling::span[1]")
    DISABLED: Final[Locator] = (By.XPATH, "//label[normalize-space()='Disabled']/following-sibling::span[1]")
    PASSWORD: Final[Locator] = (By.XPATH, "//label[normalize-space()='Password']/following::input[1]")
    CONFIRM_PASSWORD: Final[Locator] = (By.XPATH, "//label[normalize-space()='Confirm Password']/following::input[1]")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver