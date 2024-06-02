from selenium.webdriver.support.wait import WebDriverWait


class AbstractBasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(driver=self.browser, timeout=10)