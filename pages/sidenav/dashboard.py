from utils.type_checker import Locator
from utils.page_titles import PAGE_TITLE
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.common_page import CommonPage

class Dashboard:

    DASHBOARD_HEADING: Locator = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    TIME_AT_WORK:Locator =(By.XPATH, "//P[normalize-space()='Time at Work']")
    MY_ACTIONS:Locator = (By.XPATH, "//P[normalize-space()='My Actions']")
    QUICK_LAUNCH: Locator = (By.XPATH, "//P[normalize-space()='Quick Launch']")
    BUZZ_LATEST_POSTS:Locator = (By.XPATH, "//P[normalize-space()='Buzz Latest Posts']")
    EMPLOYEES_ON_LEAVE_TODAY:Locator = (By.XPATH, "//P[normalize-space()='Employees on Leave Today']")
    EMPLOYEE_DISTRIBUTION:Locator = (By.XPATH, "//P[normalize-space()='Employee Distribution by Sub Unit']")
    EMPLOYEE_DISTRIBUTION_SUB_UNIT:Locator = (By.XPATH, "//P[normalize-space()='Employee Distribution by Sub Unit']")
    EMPLOYEE_DISTRIBUTION_BY_LOCATION:Locator = (By.XPATH, "//P[normalize-space()='Employee Distribution by Location']")

    # TIME AT WORK
    ATTENDANCE_CARD_ACTION:Locator = (By.CSS_SELECTOR, "button[type='button'].orangehrm-attendance-card-action")

    # MY ACTIONS
    LEAVE_REQUEST_APPROVE:Locator = (By.CSS_SELECTOR, "button[type='button'].oxd-icon-button--success.orangehrm-report-icon")
    PENDING_SELF_APPROVE:Locator = (By.CSS_SELECTOR, "button[type='button'].oxd-icon-button--danger.orangehrm-report-icon")

    # EMPLOYEES_ON_LEAVE_TODAY
    EMPLOYEE_CARD_ICON:Locator = (By.CSS_SELECTOR, "i.oxd-icon.bi-gear-fill.orangehrm-leave-card-icon")

    # QUICK LAUNCH
    ASSIGN_LEAVE:Locator = (By.CSS_SELECTOR, "button[type='button'][title='Assign Leave']")
    LEAVE_LIST: Locator = (By.CSS_SELECTOR, "button[type='button'][title='Leave List']")
    TIME_SHEETS: Locator = (By.CSS_SELECTOR, "button[type='button'][title='Timesheets']")
    APPLY_LEAVE: Locator = (By.CSS_SELECTOR, "button[type='button'][title='Apply Leave']")
    MY_LEAVE: Locator = (By.CSS_SELECTOR, "button[type='button'][title='My Leave']")
    MY_TIME_SHEET: Locator = (By.CSS_SELECTOR, "button[type='button'][title='My Timesheet']")

    # EMPLOYEE_DISTRIBUTION_SUB_UNIT
    EMP_DIS_SUB_ENGINEERING:Locator = (By.CSS_SELECTOR, "span[title='Engineering'].oxd-text.oxd-text--span")
    EMP_DIS_SUB_HUMAN_RESOURCES: Locator = (By.CSS_SELECTOR, "span[title='Human Resources'].oxd-text.oxd-text--span")
    EMP_DIS_SUB_UNASSIGNED: Locator = (By.CSS_SELECTOR, "span[title='Unassigned'].oxd-text.oxd-text--span")

    # EMPLOYEE_DISTRIBUTION_BY_LOCATION
    EMP_DIS_BY_LOC_HQ_CA: Locator = (By.CSS_SELECTOR, "span[title='HQ - CA, USA'].oxd-text.oxd-text--span")
    EMP_DIS_BY_LOC_TEXAS_RD: Locator = (By.CSS_SELECTOR, "span[title='Texas R&D'].oxd-text.oxd-text--span")
    EMP_DIS_BY_LOC_UNASSIGNED: Locator = (By.CSS_SELECTOR, "span[title='Unassigned'].oxd-text.oxd-text--span")

    def __init__(self, selenium_driver:SeleniumDriver):
        self.selenium_driver = selenium_driver

    def validate_dashboard(self):
        self.selenium_driver.wait_until_element_present(self.DASHBOARD_HEADING)
        self.selenium_driver.wait_until_element_present(CommonPage.SIDE_NAV_INDICATOR)
        self.selenium_driver.wait_until_element_present(CommonPage.USER_DROP_DOWN)
        self.selenium_driver.wait_until_element_present(self.TIME_AT_WORK)
        self.selenium_driver.wait_until_element_present(self.MY_ACTIONS)
        self.selenium_driver.wait_until_element_present(self.QUICK_LAUNCH)
        self.selenium_driver.validate_page_title(PAGE_TITLE)
