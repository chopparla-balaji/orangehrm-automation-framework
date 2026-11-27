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
    CREATE_LOGIN_DETAILS: Final[Locator] = (By.XPATH, "//input[@type='checkbox']/parent::label")
    CANCEL: Final[Locator] = (By.XPATH, "//button[@type='button']")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")
    USERNAME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[7]")
    ENABLED: Final[Locator] = (By.XPATH, "(//form/descendant::input)[8]/parent::label")
    DISABLED: Final[Locator] = (By.XPATH, "(//form/descendant::input)[9]/parent::label")
    PASSWORD: Final[Locator] = (By.XPATH, "(//form/descendant::input)[10]")
    CONFIRM_PASSWORD: Final[Locator] = (By.XPATH, "(//form/descendant::input)[11]")
    ADD_EMPLOYEE: Final[Locator] = (By.XPATH, "//header/descendant::nav[1]/descendant::ul[1]/descendant::li[3]")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def wait_for_add_employee_to_load(self, is_landing=True, is_create_details=True) -> None:
        if is_landing:
            self.selenium_driver.element_click(self.ADD_EMPLOYEE)
        self.selenium_driver.wait_until_element_present(self.EMPLOYEE_FIRST_NAME)
        self.selenium_driver.wait_until_element_present(self.EMPLOYEE_MIDDLE_NAME)
        self.selenium_driver.wait_until_element_present(self.EMPLOYEE_LAST_NAME)
        self.selenium_driver.wait_until_element_present(self.EMPLOYEE_ID)
        if is_create_details:
            script = "arguments[0].click();"
            self.selenium_driver.execute_script(script, self.selenium_driver.find_element(AddEmployee.CREATE_LOGIN_DETAILS))
            self.selenium_driver.wait_until_element_present(self.CANCEL)
            self.selenium_driver.wait_until_element_present(self.SAVE)
            self.selenium_driver.wait_until_element_present(self.USERNAME)
            self.selenium_driver.wait_until_element_visible(self.ENABLED)
            self.selenium_driver.wait_until_element_visible(self.DISABLED)
            self.selenium_driver.wait_until_element_present(self.PASSWORD)
            self.selenium_driver.wait_until_element_present(self.CONFIRM_PASSWORD)