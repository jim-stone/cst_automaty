import pytest
from ..sso.pages import AppsPage
from .pages.projects_list import ProjectsListPage



@pytest.fixture(scope='session')
def logged_projects(chrome_browser, logged_in):
    AppsPage(chrome_browser).login_to_app('projects')
    yield ProjectsListPage(chrome_browser)
