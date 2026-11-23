from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class ContactDetails:

    STREET_1: Final[Locator] = (By.CSS_SELECTOR, "Street 1")
    STREET_2: Final[Locator] = (By.CSS_SELECTOR, "Street 2")
    CITY: Final[Locator] = (By.CSS_SELECTOR, "City")
    STATE_PROVINCE: Final[Locator] = (By.XPATH, "//State/Province")
    ZIP_POSTAL_CODE: Final[Locator] = (By.XPATH, "//Zip/Postal Code")
    COUNTRY:Final[Locator] = (By.XPATH, "//Country")
    HOME: Final[Locator] = (By.XPATH, "//Home")
    MOBILE: Final[Locator] = (By.XPATH, "//Mobile")
    WORK: Final[Locator] = (By.XPATH, "//Work")
    WORK_EMAIL: Final[Locator] = (By.XPATH, "//Work Email")
    OTHER_EMAIL: Final[Locator] = (By.XPATH, "//Other Email")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver