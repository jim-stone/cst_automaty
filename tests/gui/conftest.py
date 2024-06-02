import os
import pytest
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .sso.pages import LoginPage, AppsPage
from tests.config import ENV_NAME

load_dotenv(find_dotenv(f'.env.{ENV_NAME}'))


@pytest.fixture(scope='session')
def chrome_browser():
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
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

@pytest.fixture(scope='session')
def logged_adm(chrome_browser, logged_in):
    AppsPage(chrome_browser).login_to_app('adm')
    yield chrome_browser

@pytest.fixture
def logged_projects(chrome_browser, logged_in):
    AppsPage(chrome_browser).login_to_app('projects')
    yield chrome_browser