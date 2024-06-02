import requests
from ..conftest import url_version
from ..conftest import PROJECTS_PWD

def test_can_read_api_version(base_api_url):
    response = requests.post(base_api_url + url_version)
    expected_keys = {'wersja', 'opis', 'historiaZmian'}
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert set(response.json().keys()) == expected_keys


def test_can_read_single_dictionary_with_positions(downloaded_dictionary):
    data = downloaded_dictionary.json()
    dd = data['slowniki'][0]
    positions = dd['pozycje']
    assert downloaded_dictionary.status_code == 200
    assert downloaded_dictionary.reason == 'OK'
    assert len(positions) == dd['iloscPozycji']
    for p in positions:
        assert p['kod']
        assert p['nazwa']

def test_can_filter_projects_by_pwd(all_projects_in_pwd):
    numbers = [p['numer'] for p in all_projects_in_pwd]
    assert all([PROJECTS_PWD in n for n in numbers])
