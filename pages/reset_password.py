from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class ResetPassword:

    USERNAME: Final[Locator] = (By.NAME, "username")
    CANCEL: Final[Locator] = (By.XPATH, "//input[@name='username']/following::button[@type='button'][1]")
    RESET_PASSWORD: Final[Locator] = (By.XPATH, "//input[@name='username']/following::button[@type='button'][2]")
