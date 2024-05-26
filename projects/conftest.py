import pytest
from fixtures import chrome_browser, logged_in
from sso.pages import AppsPage


@pytest.fixture
def logged_projects(logged_in):
    AppsPage(chrome_browser).login_to_projects()
    yield chrome_browser