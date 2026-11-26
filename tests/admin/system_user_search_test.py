import allure
import pytest
from pages.login_page import LoginPage
from pages.usermenu import UserMenu
from pages.sidenav.admin.system_users import SystemUsers
from pages.sidenav.admin.user_management import UserManagement
from utils.testdata import user_name, password
from time import sleep


@allure.title("test sample")
@pytest.mark.system_user_search
class TestSystemUserSearch:

    username = user_name
    password = password
    role = 'Admin'
    name = 'Odis  Adalwin'
    status = 'Enabled'

    def test_navigate_dashboard(self, login_in):
        ...

    def test_search_user_management(self, selenium_driver):
        system_users = SystemUsers(selenium_driver)
        system_users.landing_user_management()
        system_users.search_user({'username': 'admin', 'status': self.status})

    def test_logout(self, log_out):
        ...