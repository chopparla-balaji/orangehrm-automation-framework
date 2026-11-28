from pages.sidenav_page import SideNav
from pages.sidenav.my_info.personal_details import PersonalDetails
from pages.sidenav.my_info.contact_details import ContactDetails

class TestMyInfoWebElements:

    def test_login(self, login_in):
        ...

    def test_waits_for_my_info_web_elements_load(self, selenium_driver):
        details = PersonalDetails(selenium_driver)
        details.selenium_driver.element_click(SideNav.MY_INFO)
        details.wait_for_personal_details_to_load(False)
        contact_details = ContactDetails(selenium_driver)
        contact_details.wait_contact_details_to_load()
        details.wait_for_personal_details_to_load()


    def test_logout(self, log_out):
        ...