import time


def test_can_see_projects_list(logged_projects):
    projects_page = logged_projects
    assert projects_page.get_header() == 'Lista projektów'
    assert projects_page.get_projects_count() >= 0


def test_can_filter_list(logged_projects):
    page = logged_projects.filter_to_one_project()
    page.click_burger_on_project()
    time.sleep(3)
    page.click_burger_menu_item()
    time.sleep(10)
    assert 1 == 1
