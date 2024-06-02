import os
import pytest
from .pages import LoginPage, AppsPage


@pytest.mark.skip
def test_can_login(chrome_browser, logged_in):
    login_page = LoginPage(chrome_browser, os.getenv('START_URL'))
    apps_page = AppsPage(chrome_browser)
    fullname = os.getenv('FULLNAME1')
    list_to_verify = apps_page.get_user()
    assert any([fullname in e for e in list_to_verify])
