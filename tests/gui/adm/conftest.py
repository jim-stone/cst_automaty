import pytest
from ..sso.pages import AppsPage
from .pages.adm_landing import AdmLandingPage

@pytest.fixture(scope='session')
def logged_adm(chrome_browser, logged_in):
    AppsPage(chrome_browser).login_to_app('adm')
    yield AdmLandingPage(chrome_browser)
