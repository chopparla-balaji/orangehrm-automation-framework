from typing import Final
from utils.type_checker import Locator
from utils.ui_helpers import UiHelpers
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class SharedResources:

    NO_CANCEL_BTN: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[@type='button'][1]")
    DELETE_BTN: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[@type='button'][2]")
    CLOSE_DIALOG: Final[Locator] = (By.XPATH, "//div[@role='dialog']/descendant::button[1]")
    DELETE_ACTION: Locator = (By.XPATH, "//div[normalize-space()='{entity}']/following::button[@type='button'][1]")
    UPDATE_ACTION: Locator = (By.XPATH, "//div[normalize-space()='{entity}']/following::button[@type='button'][2]")

    def __init__(self, selenium_driver: SeleniumDriver) -> None:
        self.selenium_driver = selenium_driver

    def wait_for_modal_elements_to_be_loaded(self, is_open: bool = True) -> None:
        if is_open:
            self.selenium_driver.wait_until_element_visible(self.CLOSE_DIALOG)
            self.selenium_driver.wait_until_element_visible(self.NO_CANCEL_BTN)
            self.selenium_driver.wait_until_element_visible(self.DELETE_BTN)
        else:
            self.selenium_driver.wait_until_element_in_visible(self.CLOSE_DIALOG)
            self.selenium_driver.wait_until_element_in_visible(self.NO_CANCEL_BTN)
            self.selenium_driver.wait_until_element_in_visible(self.DELETE_BTN)

    def delete_entity(self, entity_val:str) -> None:
        self.selenium_driver.window_scroll(1400)
        self.selenium_driver.element_click(UiHelpers.format_locator_text(self.DELETE_ACTION,
                                                                         {'entity': entity_val}))
        self.wait_for_modal_elements_to_be_loaded()
        self.selenium_driver.element_click(self.DELETE_BTN)
        self.wait_for_modal_elements_to_be_loaded(False)

    def update_entity(self, entity_val:str) -> None:
        self.selenium_driver.element_click(UiHelpers.format_locator_text(self.UPDATE_ACTION,
                                                                         {'entity': entity_val}))