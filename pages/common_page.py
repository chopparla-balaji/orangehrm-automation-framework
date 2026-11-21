from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class CommonPage:

    USER_DROP_DOWN: Locator = (By.CSS_SELECTOR, "ui > li.oxd-userdropdown")
    SIDE_NAV_INDICATOR:Locator = (By.CSS_SELECTOR, "button[type='button'].oxd-icon-button.oxd-main-menu-button")