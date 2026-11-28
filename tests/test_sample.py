from pages.sidenav.admin.system_users import SystemUsers
from pages.sidenav.admin.user_management import UserManagement
from pages.sidenav_page import SideNav

class TestSample:

    def test_navigate_dashboard(self, login_in):
        ...

    def test_waits_for_users_web_elements_to_load(self, selenium_driver):
        system_users = SystemUsers(selenium_driver)
        system_users.selenium_driver.element_click(SideNav.ADMIN)
        system_users.wait_for_system_user_to_load()
        user_management = UserManagement(selenium_driver)
        user_management.wait_for_add_users_to_load()
        system_users.wait_for_system_user_to_load(True)

    def test_logout(self, log_out):
        ...