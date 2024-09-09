import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '655d62f4c4623d909224fb97739136d8'
HEADER  = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '5188'

def test_status_code_trainer():
    response = requests.get(url=f'{URL}/trainers', params = {'trainer_id': TRAINER_ID })
    assert response.status_code == 200

def test_part_of_response_trainer_name():   
    response_get = requests.get(url=f'{URL}/trainers', params = {'trainer_id': TRAINER_ID })
    assert response_get.json()["data"][0]["trainer_name"] == 'Брутус'


    