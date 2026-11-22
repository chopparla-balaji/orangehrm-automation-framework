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
        system_users = SystemUsers(selenium_driver)
        system_users.landing_user_management()
        system_users.search_user({'username': self.username, 'role': self.role, 'name': self.name, 'status': self.status})
        user_manage = UserManagement(selenium_driver)
        user_manage.selenium_driver.element_click(system_users.ADD_USER)
        user_manage.validate_user_management()
        user_manage.add_user({'username': self.username, 'role': self.role, 'name': self.name, 'status': self.status,
                           'password': self.password, 'confirm_password': self.password})
        user_manage.update_user({'username': self.username, 'role': 'ESS', 'name': 'Orange  Test', 'status': 'Disabled',})
        user_manage.update_user({'username': self.username, 'role': 'Admin', 'name': 'Thomas Kutty Benny', 'status': self.status,
                              'password': self.password, 'confirm_password': self.password}, is_change_password=True)
        user_manage.delete_user(self.username)

    def test_logout(self, driver_initialization):
        selenium_driver = SeleniumDriver(driver_initialization)
        user_menu = UserMenu(selenium_driver)
        user_menu.logout_orm()
        login_page = LoginPage(selenium_driver)
        login_page.validate_loin_page()