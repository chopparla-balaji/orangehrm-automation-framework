from pages.login_page import LoginPage
from pages.reset_password import ResetPassword

class TestResetPasswordWebElementsWaits:

    def test_waits_for_reset_password_web_elements_load(self, selenium_driver):
        login_page = LoginPage(selenium_driver)
        login_page.open_orangehrm()
        reset_password = ResetPassword(selenium_driver)
        reset_password.wait_for_reset_password_to_load()