from pages.sidenav.sidenav import SideNav
from pages.sidenav.time import ManageTime

class TestTimeWebElementWaits:

    def test_login(self, login_in):
        ...

    def test_waits_for_time_web_elements_load(self, selenium_driver):
        manage_time = ManageTime(selenium_driver)
        manage_time.selenium_driver.element_click(SideNav.TIME)
        manage_time.wait_for_time_sheet_to_load()
        manage_time.wait_for_employee_attendance_rec_to_load()
        manage_time.wait_for_employee_reports_to_load()
        manage_time.wait_for_customers_to_load()

    def test_logout(self, log_out):
        ...