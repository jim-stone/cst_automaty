import os
import time

from fixtures import chrome_browser, logged_in, logged_adm
from sso.pages import LoginPage, AppsPage


def test_can_login(chrome_browser, logged_in):
    login_page = LoginPage(chrome_browser, os.getenv('START_URL'))
    apps_page = AppsPage(chrome_browser)
    fullname = os.getenv('FULLNAME1')
    list_to_verify = apps_page.get_user()
    assert any([fullname in e for e in list_to_verify])

