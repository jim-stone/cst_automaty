import os
import pytest
import requests
from dotenv import load_dotenv, find_dotenv
from templates.slownik import basic_with_positions
from utils import ENV_NAME

load_dotenv(find_dotenv(f'.env.{ENV_NAME}'))
url_token = 'api/Token'
url_version = 'api/Wersja'
url_slownik = 'api/Slownik'

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

