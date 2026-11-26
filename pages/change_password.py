from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class ChangePassword:

    CURRENT_PASSWORD : Final[Locator] = (By.XPATH, "(//form/descendant::input)[1]")
    PASSWORD: Final[Locator] = (By.XPATH, "(//form/descendant::input)[2]")
    CONFIRM_PASSWORD: Final[Locator] = (By.XPATH, "(//form/descendant::input)[3]")
    CANCEL: Final[Locator] = (By.XPATH, "//button[@type='button']")
    SAVE: Final[Locator] = (By.XPATH, "//button[@type='submit']")