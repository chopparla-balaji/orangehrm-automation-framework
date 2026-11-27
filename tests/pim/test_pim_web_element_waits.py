from pages.sidenav.sidenav import SideNav
from pages.sidenav.pim.add_employee import AddEmployee
from pages.sidenav.pim.employee_list import EmployeeList
from pages.sidenav.pim.reports import ManageReports
from pages.sidenav.pim.configuration import ManageConfiguration

class TestPimWebElementWaits:

    def test_login(self, login_in):
        ...

    def test_waits_for_pim_web_elements_load(self, selenium_driver):
        emp_list = EmployeeList(selenium_driver)
        emp_list.selenium_driver.element_click(SideNav.PIM)
        emp_list.wait_for_employee_list_to_load(False)
        add_employee = AddEmployee(selenium_driver)
        add_employee.wait_for_add_employee_to_load()
        reports = ManageReports(selenium_driver)
        reports.wait_for_reports_to_load()
        reports.wait_for_add_report_to_load()
        configuration = ManageConfiguration(selenium_driver)
        configuration.wait_for_optional_fields_to_load()
        configuration.wait_for_custom_fields_to_load()
        configuration.wait_for_add_custom_fields_to_load()
        emp_list.wait_for_employee_list_to_load()

    def test_logout(self, log_out):
        ...