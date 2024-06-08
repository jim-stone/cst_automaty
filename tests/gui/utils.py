from selenium.webdriver.support.wait import WebDriverWait
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from selenium.webdriver import Chrome


class AbstractBasePage:
    def __init__(self, browser: 'Chrome'):
        self.browser = browser
        self.wait = WebDriverWait(driver=self.browser, timeout=10)
