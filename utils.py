from selenium.webdriver.support.wait import WebDriverWait

# change this constant to run tests in a different environment
ENV_NAME = 'release'

class AbstractBasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(driver=self.browser, timeout=10)