import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '655d62f4c4623d909224fb97739136d8'
HEADER  = {'Content-Type': 'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "pytest1",
    "photo_id": 1
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json())'''


body_change = {
    "pokemon_id": "69309",
    "name": "pytest3",
    "photo_id": 2
}

'''responce_body_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(responce_body_change.json())'''

body_add_pokeball = {
    "pokemon_id": "69309"
}

responce_body_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(responce_body_add_pokeball.json())