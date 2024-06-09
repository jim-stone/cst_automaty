import os
import pytest
import requests
import random
import string
from dotenv import load_dotenv, find_dotenv
from .templates.slownik import basic_with_positions
from ..config import ENV_NAME

load_dotenv(find_dotenv(f'.env.{ENV_NAME}'))
PROJECTS_PWD = 'FESW.01.01'
url_token = 'api/Token'
url_version = 'api/Wersja'
url_slownik = 'api/Slownik'
url_projects = 'api/Projekt'


def generate_random_string(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def repeat_request_while_pages_left(url, req_data, resp_key):
    # req_data: url & json
    result = []
    response = requests.post(url=url, json=req_data)
    data = response.json()
    while data[resp_key]:
        response = requests.post(url=url, json=req_data)
        data = response.json()
        result.extend(data[resp_key])
        req_data['strona'] += 1
    return result


@pytest.fixture(scope='session')
def base_api_url():
    return os.getenv('API_BASE_URL')

@pytest.fixture(scope='session')
def token(base_api_url):
    response = requests.post(
        url=base_api_url+url_token,
        headers={os.getenv('API_GETTOKEN_HEADER'): os.getenv('API_KEY')})
    return response.json()['token']

@pytest.fixture(scope='session',
                params=['Cel polityki', 'Forma wsparcia', 'Program'])
def downloaded_dictionary(base_api_url, token, request):
    req_data = basic_with_positions
    req_data['token'] = token
    req_data['nazwySlownikow'][0] = request.param
    response = requests.post(
        url=base_api_url+url_slownik,
        json=req_data)
    return response


@pytest.fixture
def all_projects_in_pwd(base_api_url, token):
    req_url = base_api_url + url_projects
    req_data = {
        'token': token,
        'pelneInformacje': False,
        'poziomyWdrazania': [PROJECTS_PWD],
        'strona': 1}
    return repeat_request_while_pages_left(
        url=req_url, req_data=req_data, resp_key='projekty')

class ProjectGenerator():
    def __init__(self, base_list_of_projects):
        self.projects = base_list_of_projects
        self.numbers = [p['numer'] for p in self.projects]
        self.string_generator = generate_random_string
    def _create_unique_project_number(self):
        unique_parts = [n[-7:-3] for n in self.numbers]
        new_unique_number_part = self.string_generator(4)
        while new_unique_number_part in unique_parts:
            new_unique_number_part = self.string_generator(4)
        new_project_number = self.projects[0]['numer'].replace(unique_parts[0], new_unique_number_part)
        print(new_project_number)
        return new_project_number
    def _find_base_project_data_with_agreement(self):
        projects_with_agreements = [
            p for p in self.projects if p['status'] == 'UmowaPodpisana'
        ]


