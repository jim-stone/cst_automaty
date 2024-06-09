import time


def test_can_see_projects_list(logged_projects):
    projects_page = logged_projects
    assert projects_page.get_header() == 'Lista projektów'
    assert projects_page.get_projects_count() >= 0


def test_can_filter_list(logged_projects):
    page = logged_projects.filter_to_one_project()
    time.sleep(4) #semms like previous click not finished and covers next
    page.click_burger_on_project().navigate_to_project_details()
    time.sleep(6)
    assert 1 == 1
