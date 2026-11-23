from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class CommonPage:

    USER_DROP_DOWN: Final[Locator] = (By.CSS_SELECTOR, "header div:nth-child(1) div:nth-child(3) > ul > li "
                                                       "span:nth-child(1)")
    SIDE_NAV_INDICATOR: Final[Locator] = (By.CSS_SELECTOR, "button[type='button'][role='none']")