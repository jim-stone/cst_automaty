from ..conftest import ProjectGenerator


def test_can_create_new_project(all_projects_in_pwd):
    pg = ProjectGenerator(all_projects_in_pwd)
    pg.create_unique_project_number()
    assert 1==1