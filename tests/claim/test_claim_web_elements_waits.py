from pages.sidenav_page import SideNav
from pages.sidenav.claim import ManageClaims

class TestClaimWebElementsWaits:

    def test_login(self, login_in):
        ...

    def test_waits_for_claim_web_elements_load(self, selenium_driver):
        claim = ManageClaims(selenium_driver)
        claim.selenium_driver.element_click(SideNav.CLAIM)
        claim.wait_for_employee_claims_to_load()
        claim.wait_for_assign_claims_to_load()
        claim.wait_for_my_claims_to_load()


    def test_logout(self, log_out):
        ...