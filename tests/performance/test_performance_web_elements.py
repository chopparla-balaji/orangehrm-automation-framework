from pages.sidenav.sidenav import SideNav
from pages.sidenav.performance import EmployeePerformance

class TestPerformanceWebElementWaits:

    def test_login(self, login_in):
        ...

    def test_waits_for_performance_web_elements_load(self, selenium_driver):
        employee_performance = EmployeePerformance(selenium_driver)
        employee_performance.selenium_driver.element_click(SideNav.PERFORMANCE)
        employee_performance.wait_for_employee_reviewers_to_load()
        employee_performance.wait_for_employee_trackers_to_load()
        employee_performance.wait_for_employee_reviewers_to_load()

    def test_logout(self, log_out):
        ...