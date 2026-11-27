from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class ContactDetails:

    STREET_1: Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    STREET_2: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    CITY: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    STATE_PROVINCE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[4]")
    ZIP_POSTAL_CODE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[5]")
    COUNTRY:Final[Locator] = (By.XPATH, "(//div[@tabIndex='0'])[1]/ancestor::div[2]")
    HOME: Final[Locator] = (By.XPATH, "(//form/descendant::input)[6]")
    MOBILE: Final[Locator] = (By.XPATH, "(//form/descendant::input)[7]")
    WORK: Final[Locator] = (By.XPATH, "(//form/descendant::input)[8]")
    WORK_EMAIL: Final[Locator] = (By.XPATH, "(//form/descendant::input)[9]")
    OTHER_EMAIL: Final[Locator] = (By.XPATH, "(//form/descendant::input)[10]")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")

    CONTACT_DETAILS:Final[Locator] = (By.XPATH, "//div[@role='tablist']/div[2]/a")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def wait_contact_details_to_load(self, is_contact_details_loaded: bool=True) -> None:
        if is_contact_details_loaded:
            self.selenium_driver.element_click(self.CONTACT_DETAILS)
        self.selenium_driver.wait_until_element_present(self.STREET_1)
        self.selenium_driver.wait_until_element_present(self.STREET_2)
        self.selenium_driver.wait_until_element_present(self.CITY)
        self.selenium_driver.wait_until_element_present(self.STATE_PROVINCE)
        self.selenium_driver.wait_until_element_present(self.ZIP_POSTAL_CODE)
        self.selenium_driver.wait_until_element_present(self.COUNTRY)
        self.selenium_driver.wait_until_element_present(self.HOME)
        self.selenium_driver.wait_until_element_present(self.MOBILE)
        self.selenium_driver.wait_until_element_present(self.WORK)
        self.selenium_driver.wait_until_element_present(self.WORK_EMAIL)
        self.selenium_driver.wait_until_element_present(self.OTHER_EMAIL)
        self.selenium_driver.wait_until_element_present(self.SAVE)