from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class AddEmployee:

    ADD_EMPLOYEE_PIC: Final[Locator] = (By.CSS_SELECTOR, "input[type='file']")
    EMPLOYEE_FIRST_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='firstName'][placeholder='First Name']")
    EMPLOYEE_MIDDLE_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='middleName'][placeholder='Middle Name']")
    EMPLOYEE_LAST_NAME: Final[Locator] = (By.CSS_SELECTOR, "input[name='lastName'][placeholder='Last Name']")
    EMPLOYEE_ID: Final[Locator] = (By.XPATH, "(//form/descendant::input)[5]")
    CREATE_LOGIN_DETAILS: Final[Locator] = (By.XPATH, "(//form/descendant::input)[6]/following::span[1]")
    CANCEL: Final[Locator] = (By.XPATH, "//button[@type='button']")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")
    USERNAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[7]")
    ENABLED: Final[Locator] = (By.XPATH, "(//form/input[@type='radio'])[1]")
    DISABLED: Final[Locator] = (By.XPATH, "(//form/input[@type='radio'])[2]")
    PASSWORD: Final[Locator] = (By.XPATH, "(//form/input[@type='password'])[1]")
    CONFIRM_PASSWORD: Final[Locator] = (By.XPATH, "(//form/input[@type='password'])[2]")
    ADD_EMPLOYEE: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver