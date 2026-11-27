from pages.change_password import ChangePassword

class TestChangePasswordWebElementsWaits:

    def test_login(self, login_in):
        ...

    def test_waits_for_change_password_web_elements_load(self, selenium_driver):
        change_password = ChangePassword(selenium_driver)
        change_password.wait_for_change_password_to_load()