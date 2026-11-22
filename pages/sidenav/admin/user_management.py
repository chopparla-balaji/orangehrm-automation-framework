from typing import Final
from utils.type_checker import Locator, ADD_USER, EDIT_USER
from utils.page_titles import PAGE_TITLE
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.sidenav.admin.system_users import SystemUsers
from utils.constants import USER_NAME, PASSWORD, CONFIRM_PASSWORD, NAME, ROLE, STATUS

class UserManagement:

    ADD_USER_HEADING: Final[Locator] = (By.XPATH, "//h6[normalize-space()='Add User']")
    USER_ROLE: Final[Locator] = (By.XPATH, "//label[text()='User Role']/ancestor::div[2]/descendant::div[2]/div[1]")
    EMPLOYEE_NAME: Final[Locator] = (By.XPATH, "//label[text()='Employee Name']/following::input[@placeholder='Type "
                                               "for hints...'][1]")
    USERNAME: Final[Locator] = (By.XPATH, "//label[text()='Username']/ancestor::div[2]/descendant::input[1]")
    STATUS: Final[Locator] = (By.XPATH, "//label[text()='Status']/ancestor::div[2]/descendant::div[2]/div[1]")
    PASSWORD: Final[Locator] = (By.XPATH, "//label[normalize-space()='Password']/following::input[@type='password' "
                                          "and @autocomplete='off'][1]")
    CONFIRM_PASSWORD: Final[Locator] = (By.XPATH, "//label[normalize-space()='Confirm Password']/following::input"
                                                  "[@type='password' and @autocomplete='off'][1]")
    CANCEL: Final[Locator] = (By.XPATH, "//button[normalize-space()='Cancel'][@type='button']")
    SAVE: Final[Locator] = (By.XPATH, "//button[normalize-space()='Save'][@type='submit']")

    # Option Value
    OPT_VAL: Final[Locator] = (By.XPATH, "//span[normalize-space()='{option}']/parent::div[@role='option']")

    # Edit User
    EDIT_USER_HEADING: Final[Locator] = (By.XPATH, "//h6[normalize-space()='Edit User']")
    CHANGE_PASSWORD: Final[Locator] = (By.XPATH, "//label[normalize-space()='Change Password ?']/"
                                                 "following::input[@type='checkbox'][1]")

    # Messages
    SUC_MSG_HEADING:Final[Locator] = (By.XPATH, "//p[normalize-space()='Success']")
    ADD_USER_MSG:Final[Locator] = (By.XPATH, "//p[normalize-space()='Successfully Saved']")
    UPDATE_USER_MSG:Final[Locator] = (By.XPATH, "//p[normalize-space()='Successfully Updated']")
    DELETE_USER_MSG:Final[Locator] = (By.XPATH, "//p[normalize-space()='Successfully Deleted']")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def validate_user_management(self, is_add=True) -> None:
        if is_add:
            self.selenium_driver.wait_until_element_present(self.ADD_USER_HEADING)
        self.selenium_driver.wait_until_element_present(self.USERNAME)
        self.selenium_driver.wait_until_element_present(self.USER_ROLE)
        self.selenium_driver.wait_until_element_present(self.STATUS)
        self.selenium_driver.wait_until_element_present(self.EMPLOYEE_NAME)
        if is_add:
            self.selenium_driver.wait_until_element_present(self.PASSWORD)
            self.selenium_driver.wait_until_element_present(self.CONFIRM_PASSWORD)
        self.selenium_driver.wait_until_element_present(self.CANCEL)
        self.selenium_driver.wait_until_element_present(self.SAVE)
        self.selenium_driver.validate_page_title(PAGE_TITLE)

    def add_user(self, user_details:dict[str, str]) -> None:
        # user details contains [role, name, status, username, password, confirm_password] [Give Dict keys all mandatory]
        self.user_management(user_details)

    def update_user(self, user_details:dict[str, str], is_change_password=False) -> None:
        user_manage = SystemUsers(self.selenium_driver)
        user_manage.selenium_driver.window_scroll(1400)
        if USER_NAME in user_details:
            update_action = (user_manage.UPDATE_ACTION[0], user_manage.UPDATE_ACTION[1]
                             .format(username=user_details[USER_NAME]))
            user_manage.selenium_driver.element_click(update_action)
            self.validate_user_management(False)
            self.user_management(user_details, False, is_change_password)
        else:
            raise KeyError("Missing required fields of username")

    def delete_user(self, user_name:str) -> None:
        user_manage = SystemUsers(self.selenium_driver)
        delete_action = (user_manage.DELETE_ACTION[0], user_manage.DELETE_ACTION[1].format(username=user_name))
        user_manage.selenium_driver.window_scroll(1400)
        user_manage.selenium_driver.element_click(delete_action)
        user_manage.selenium_driver.wait_until_element_visible(user_manage.NO_CANCEL_USER)
        user_manage.selenium_driver.wait_until_element_visible(user_manage.DELETE_USER)
        user_manage.selenium_driver.element_click(user_manage.DELETE_USER)
        user_manage.selenium_driver.wait_until_element_in_visible(user_manage.NO_CANCEL_USER)
        user_manage.selenium_driver.wait_until_element_in_visible(user_manage.DELETE_USER)
        self.selenium_driver.wait_until_element_visible(self.SUC_MSG_HEADING, 40)
        self.selenium_driver.wait_until_element_visible(self.DELETE_USER_MSG, 40)
        user_manage.selenium_driver.window_scroll(-1400)
        user_manage.validate_system_user()

    def user_management(self, manage_user_details:dict[str, str], is_add=True, is_change_password=False) -> None:
        user_manage = SystemUsers(self.selenium_driver)
        if all(key in manage_user_details for key in (ADD_USER if is_add or
                                                                  (not is_add and is_change_password) else EDIT_USER)):
            self.selenium_driver.element_click(self.USER_ROLE)
            self.selenium_driver.select_option_element(self.OPT_VAL, manage_user_details[ROLE], 40)
            self.selenium_driver.send_keys(self.EMPLOYEE_NAME, manage_user_details[NAME])
            self.selenium_driver.select_option_element(self.OPT_VAL, manage_user_details[NAME], 40)
            self.selenium_driver.element_click(self.STATUS)
            self.selenium_driver.select_option_element(self.OPT_VAL, manage_user_details[STATUS], 40)
            self.selenium_driver.send_keys(self.USERNAME, manage_user_details[USER_NAME])
            if is_add or is_change_password:
                if is_change_password:
                    self.selenium_driver.wait_until_element_visible(self.PASSWORD)
                    self.selenium_driver.wait_until_element_visible(self.CONFIRM_PASSWORD)
                self.selenium_driver.send_keys(self.PASSWORD, manage_user_details[PASSWORD])
                self.selenium_driver.send_keys(self.CONFIRM_PASSWORD, manage_user_details[CONFIRM_PASSWORD])
            self.selenium_driver.element_click(self.SAVE)
            self.selenium_driver.wait_until_element_visible(self.SUC_MSG_HEADING, 40)
            if is_add:
                self.selenium_driver.wait_until_element_visible(self.ADD_USER_MSG, 40)
            else:
                self.selenium_driver.wait_until_element_visible(self.UPDATE_USER_MSG, 40)
            user_manage.validate_system_user()
            delete_action = (user_manage.DELETE_ACTION[0], user_manage.DELETE_ACTION[1]
                             .format(username=manage_user_details[USER_NAME]))
            update_action = (user_manage.UPDATE_ACTION[0], user_manage.UPDATE_ACTION[1]
                             .format(username=manage_user_details[USER_NAME]))
            user_manage.selenium_driver.window_scroll(1400)
            self.selenium_driver.wait_until_element_present(delete_action)
            self.selenium_driver.wait_until_element_present(update_action)
        else:
            missing_fields = [key for key in ADD_USER if key not in manage_user_details]
            raise KeyError(f"Missing required fields: {missing_fields}")
