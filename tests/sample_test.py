from base.selenium_driver import SeleniumDriver
from pages.login_page import LoginPage
from pages.sidenav.dashboard import Dashboard
from pages.usermenu import UserMenu

class TestSample:

    def test_navigate_dashboard(self, driver_initialization):
        selenium_driver = SeleniumDriver(driver_initialization)
        login_page = LoginPage(selenium_driver)
        login_page.open_orangehrm()
        login_page.enter_credentials()
        login_page.selenium_driver.element_click(login_page.LOGIN_BTN)
        dashboard = Dashboard(selenium_driver)
        dashboard.validate_dashboard()

    def test_logout(self, driver_initialization):
        selenium_driver = SeleniumDriver(driver_initialization)
        user_menu = UserMenu(selenium_driver)
        user_menu.logout_orm()
        login_page = LoginPage(selenium_driver)
        login_page.validate_loin_page()