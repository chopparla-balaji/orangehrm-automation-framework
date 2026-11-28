from pages.sidenav_page import SideNav
from pages.sidenav.recruitment import ManageRecruitment

class TestRecruitmentWebElementWaits:

    def test_login(self, login_in):
        ...

    def test_waits_for_recruitment_web_elements_load(self, selenium_driver):
        rec = ManageRecruitment(selenium_driver)
        rec.selenium_driver.element_click(SideNav.RECRUITMENT)
        rec.wait_for_candidates_to_load()
        rec.wait_for_add_page_candidates_to_load()

    def test_logout(self, log_out):
        ...