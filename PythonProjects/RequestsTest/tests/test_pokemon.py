import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json',}
TOKEN = '05b9f7ed87a1999a216b6b6ddefc49c8'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {"level" : 1})
    assert response.status_code == 200

def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 2670})
    assert response.json()['data'][0]['trainer_name'] == 'Хлоя'






