import os
import pytest
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .sso.pages import LoginPage, AppsPage
from tests.config import ENV_NAME

load_dotenv(find_dotenv(f'.env.{ENV_NAME}'))


@pytest.fixture(scope='session')
def chrome_browser():
    options = Options()
    if os.getenv('IS_HEADLESS') == 'true':
        options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service, options=options)
    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def logged_in(chrome_browser):
    login = os.getenv('LOGIN1')
    password = os.getenv('PASS1')
    url = os.getenv('START_URL')
    LoginPage(chrome_browser, url).open().login(login, password)
    yield chrome_browser
