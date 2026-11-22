import allure
import pytest
from base.selenium_driver import SeleniumDriver
from pages.login_page import LoginPage
from pages.sidenav.dashboard import Dashboard
from pages.usermenu import UserMenu
from pages.sidenav.admin.system_users import SystemUsers
from pages.sidenav.admin.user_management import UserManagement
from utils.testdata import user_name, password


@allure.title("test sample")
@pytest.mark.user_management
class TestUserManagement:

    username = user_name
    password = password
    role = 'Admin'
    name = 'Orange  Test'
    status = 'Enabled'

    def test_navigate_dashboard(self, driver_initialization):
        selenium_driver = SeleniumDriver(driver_initialization)
        login_page = LoginPage(selenium_driver)
        login_page.open_orangehrm()
        login_page.enter_credentials()
        login_page.selenium_driver.element_click(login_page.LOGIN_BTN)
        dashboard = Dashboard(selenium_driver)
        dashboard.validate_dashboard()

    def test_validate_user_management(self, driver_initialization):
        selenium_driver = SeleniumDriver(driver_initialization)
        user_management = SystemUsers(selenium_driver)
        user_management.landing_user_management()
        user_management.search_user({'username': self.username, 'role': self.role, 'name': self.name, 'status': self.status})
        add_user = UserManagement(selenium_driver)
        add_user.selenium_driver.element_click(user_management.ADD_USER)
        add_user.validate_user_management()
        add_user.add_user({'username': self.username, 'role': self.role, 'name': self.name, 'status': self.status,
                           'password': self.password, 'confirm_password': self.password})
        add_user.update_user({'username': self.username, 'role': 'ESS', 'name': 'Orange  Test', 'status': 'Disabled',})
        add_user.update_user({'username': self.username, 'role': 'Admin', 'name': 'Thomas Kutty Benny', 'status': self.status,
                              'password': self.password, 'confirm_password': self.password}, is_change_password=True)
        add_user.delete_user(self.username)

    def test_logout(self, driver_initialization):
        selenium_driver = SeleniumDriver(driver_initialization)
        user_menu = UserMenu(selenium_driver)
        user_menu.logout_orm()
        login_page = LoginPage(selenium_driver)
        login_page.validate_loin_page()