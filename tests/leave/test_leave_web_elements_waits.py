from pages.sidenav.sidenav import SideNav
from pages.sidenav.leave.assign_leave import AssignLeave
from pages.sidenav.leave.configures import Configures

class TestLeaveWebElementsWaits:

    def test_login(self, login_in):
        ...

    def test_waits_for_leave_web_elements_load(self, selenium_driver):
        assign_leave = AssignLeave(selenium_driver)
        assign_leave.selenium_driver.element_click(SideNav.LEAVE)
        assign_leave.wait_for_leave_list_to_load()
        assign_leave.wait_for_assign_leave_to_load()
        config = Configures(selenium_driver)
        config.wait_for_leave_period_to_load()
        config.wait_for_work_week_to_load()

    def test_logout(self, log_out):
        ...