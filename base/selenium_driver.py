from typing import Callable
from base.base_driver import BaseDriver
from utils.page_titles import PAGE_TITLE
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from utils.constants import IMPLICIT_WAIT, EXPLICIT_WAIT, VISIBLE_TEXT, VALUE, INDEX


class SeleniumDriver(BaseDriver):

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url:str) -> None:
        self.driver.get(url)

    def find_element(self, locator:tuple[str,str]) -> WebElement:
        self.implicit_wait()
        web_element = self.driver.find_element(*locator)
        return web_element

    def find_elements(self, locator:tuple[str,str]) -> list[WebElement]:
        self.implicit_wait()
        web_elements = self.driver.find_elements(*locator)
        return web_elements

    def send_keys(self, locator:tuple[str,str], value:str | int) -> None:
        web_element = self.find_element(locator)
        web_element.clear()
        web_element.send_keys(value)

    def element_click(self, locator:tuple[str,str]) -> None:
        self.find_element(locator).click()

    def execute_script(self, script:str) -> None:
        self.driver.execute_script(script)

    def validate_page_title(self) -> None:
        assert self.driver.title == PAGE_TITLE

    def window_scroll(self, scroll_val:int) -> None:
        self.implicit_wait()
        self.execute_script(f"window.scrollTo(0, {scroll_val})")

    def scroll_into_view(self, locator:tuple[str,str]) -> None:
        web_element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", web_element)

    def implicit_wait(self, timeout=IMPLICIT_WAIT):
        self.driver.implicitly_wait(timeout)

    def upload_file(self, locator:tuple[str,str], file:str) -> None:
        self.find_element(locator).send_keys(file)

    def select_dropdown_option(self, locator:tuple[str,str], value:str | int, select_type=VISIBLE_TEXT) -> None:
        web_element = self.find_element(locator)
        if select_type == VISIBLE_TEXT:
            Select(web_element).select_by_visible_text(value)
        elif select_type == VALUE:
            Select(web_element).select_by_value(value)
        elif select_type == INDEX and type(value) is int:
            Select(web_element).select_by_index(int(value))

    def field_results(self, locator:tuple[str,str], value:str | int) -> None:
        web_element = self.find_element(locator)
        web_element.clear()
        web_element.send_keys(value)
        web_element.send_keys(Keys.ENTER)

    def select_option_element(self, locator:tuple[str,str], value:str | int, timeout=EXPLICIT_WAIT) -> None:
        opt_value = (locator[0], locator[1].format(option=value))
        self.wait_until_element_visible(opt_value, timeout=timeout)
        web_element = self.find_element(opt_value)
        web_element.click()

    def wait_until_element_clickable(self, locator:tuple[str,str], timeout=EXPLICIT_WAIT) -> None:
        self.web_driver_wait(ec.element_to_be_clickable(locator), timeout)

    def wait_until_element_present(self, locator:tuple[str,str], timeout=EXPLICIT_WAIT) -> None:
        self.web_driver_wait(ec.presence_of_element_located(locator), timeout)

    def wait_until_element_visible(self, locator:tuple[str,str], timeout=EXPLICIT_WAIT) -> None:
        self.web_driver_wait(ec.visibility_of_element_located(locator), timeout)

    def wait_until_element_in_visible(self, locator:tuple[str, str],timeout=EXPLICIT_WAIT) -> None:
        self.web_driver_wait(ec.invisibility_of_element_located(locator), timeout)

    def wait_until_frame_available_and_switch(self, locator:tuple[str,str], timeout=EXPLICIT_WAIT) -> None:
        self.web_driver_wait(ec.frame_to_be_available_and_switch_to_it(locator), timeout)

    def web_driver_wait(self, expected_condition:Callable, timeout=EXPLICIT_WAIT) -> None:
        web_driver_wait = WebDriverWait(self.driver, timeout)
        web_driver_wait.until(expected_condition)