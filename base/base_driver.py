from abc import ABC, abstractmethod
from utils.constants import IMPLICIT_WAIT, EXPLICIT_WAIT, VISIBLE_TEXT
from selenium.webdriver.remote.webelement import WebElement

class BaseDriver(ABC):

    @abstractmethod
    def find_element(self, locator:tuple[str,str]) -> WebElement:
        ...

    @abstractmethod
    def open_url(self, url:str) -> None:
        ...

    @abstractmethod
    def find_elements(self, locator:tuple[str,str]) -> list[WebElement]:
        ...

    @abstractmethod
    def send_keys(self, locator:tuple[str,str], value:str | int) -> None:
        ...

    @abstractmethod
    def element_click(self, locator:tuple[str,str]) -> None:
        ...

    @abstractmethod
    def execute_script(self, script:str) -> None:
        ...

    @abstractmethod
    def validate_page_title(self) -> None:
        ...

    @abstractmethod
    def window_scroll(self, scroll_val:int) -> None:
        ...

    @abstractmethod
    def scroll_into_view(self, locator:tuple[str,str]) -> None:
        ...

    @abstractmethod
    def implicit_wait(self, timeout=IMPLICIT_WAIT) -> None:
        ...

    @abstractmethod
    def upload_file(self, locator:tuple[str,str], file:str) -> None:
        ...

    @abstractmethod
    def select_dropdown_option(self, locator:tuple[str,str], value:str | int, select_type=VISIBLE_TEXT) -> None:
        ...

    @abstractmethod
    def field_results(self, locator:tuple[str,str], value:str | int) -> None:
        ...

    @abstractmethod
    def select_option_element(self, locator:tuple[str,str], value:str | int, timeout=EXPLICIT_WAIT) -> None:
        ...

    @abstractmethod
    def wait_until_element_clickable(self, locator:tuple[str,str], timeout=EXPLICIT_WAIT) -> None:
        ...

    @abstractmethod
    def wait_until_element_present(self, locator:tuple[str,str], timeout=EXPLICIT_WAIT) -> None:
        ...

    @abstractmethod
    def wait_until_element_visible(self, locator:tuple[str,str], timeout=EXPLICIT_WAIT) -> None:
        ...

    @abstractmethod
    def wait_until_element_in_visible(self, locator:tuple[str,str], timeout=EXPLICIT_WAIT) -> None:
        ...

    @abstractmethod
    def wait_until_frame_available_and_switch(self, locator:tuple[str,str], timeout=EXPLICIT_WAIT) -> None:
        ...