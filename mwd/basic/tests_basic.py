import requests
from mwd.conftest import url_version


def test_can_get_api_version(base_api_url):
    response = requests.post(base_api_url + url_version)
    expected_keys = {'wersja', 'opis', 'historiaZmian'}
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert set(response.json().keys()) == expected_keys


def test_can_download_single_dictionary_with_positions(downloaded_dictionary):
    data = downloaded_dictionary.json()
    dd = data['slowniki'][0]
    positions = dd['pozycje']
    assert downloaded_dictionary.status_code == 200
    assert downloaded_dictionary.reason == 'OK'
    assert len(positions) == dd['iloscPozycji']
    for p in positions:
        assert p['kod']
        assert p['nazwa']
