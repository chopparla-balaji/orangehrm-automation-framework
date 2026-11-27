from pages.login_page import LoginPage
from pages.sidenav.sidenav import SideNav
from pages.sidenav.leave.assign_leave import AssignLeave
from pages.sidenav.leave.configures import Configures
from pages.change_password import ChangePassword

class TestSample:

    def test_login(self, login_in):
        ...

    def test_action(self, selenium_driver):
        change_password = ChangePassword(selenium_driver)
        change_password.wait_for_change_password_to_load()

    # def test_logout(self, log_out):
    #     ...