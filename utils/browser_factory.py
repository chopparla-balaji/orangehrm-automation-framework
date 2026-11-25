from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.constants import (WINDOW_SIZE, DISABLE_NOTIFICATIONS, DISABLE_DEV_SHM_USAGE, HEALENIUM_URL, HEADLESS_NEW,
                             HEADLESS, NO_SANDBOX, CHROME, FIREFOX, EDGE)


BROWSER_OPTIONS = {
    CHROME: ChromeOptions,
    EDGE: EdgeOptions,
    FIREFOX: FirefoxOptions
}

BROWSER_DRIVERS = {
    CHROME: webdriver.Chrome,
    EDGE: webdriver.Edge,
    FIREFOX: webdriver.Firefox
}

def browser_init(browser_name=FIREFOX, is_heal=False):
    options = BROWSER_OPTIONS.get(browser_name, FirefoxOptions)()
    options.add_argument(WINDOW_SIZE)
    options.add_argument(DISABLE_NOTIFICATIONS)
    if browser_name in (CHROME, EDGE):
        # options.add_argument(HEADLESS_NEW)
        options.add_argument(NO_SANDBOX)
        options.add_argument(DISABLE_DEV_SHM_USAGE)
    # else:
    #     options.add_argument(HEADLESS)
    if is_heal:
        return webdriver.Remote(
            command_executor=HEALENIUM_URL,
            options=options,
        )
    return BROWSER_DRIVERS.get(browser_name, webdriver.Firefox)(options=options)