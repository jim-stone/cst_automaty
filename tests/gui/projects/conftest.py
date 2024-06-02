import pytest
from ..sso.pages import AppsPage


@pytest.fixture
def logged_projects(chrome_browser, logged_in):
    AppsPage(chrome_browser).login_to_app('projects')
    yield chrome_browser
