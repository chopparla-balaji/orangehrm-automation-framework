from typing import Final
from utils.type_checker import Locator
from selenium.webdriver.common.by import By

class SideNav:

    SIDE_NAV_INDICATOR: Final[Locator] = (By.XPATH, "//nav/descendant::button[@type='button'][@role='none']")
    SEARCH: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::input[1]")
    ADMIN: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::ul[1]/descendant::li[1]/child::a")
    PIM: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::ul[1]/descendant::li[2]/child::a")
    LEAVE: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::ul[1]/descendant::li[3]/child::a")
    TIME: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::ul[1]/descendant::li[4]/child::a")
    RECRUITMENT: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::ul[1]/descendant::li[5]/child::a")
    MY_INFO: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::ul[1]/descendant::li[6]/child::a")
    PERFORMANCE: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::ul[1]/descendant::li[7]/child::a")
    DASHBOARD: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::ul[1]/descendant::li[8]/child::a")
    CLAIM: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::ul[1]/descendant::li[11]/child::a")
    BUZZ: Final[Locator] = (By.XPATH, "//nav[@role='navigation']/descendant::ul[1]/descendant::li[12]/child::a")