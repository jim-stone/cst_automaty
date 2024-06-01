from conftest import chrome_browser,logged_in
from projects.pages.projects_list import ProjectsListPage
from sso.pages import AppsPage


def test_can_see_projects_list(chrome_browser, logged_in):
    apps_page = AppsPage(chrome_browser)
    projects_page = apps_page.login_to_app('projects')
    assert projects_page.get_header() == 'Lista projektów'
    assert projects_page.get_projects_count() >= 0
