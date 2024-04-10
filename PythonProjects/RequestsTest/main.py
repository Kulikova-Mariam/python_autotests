import requests

URL = 'https://api.pokemonbattle.me/v2'

HEADERS = {'Content-Type' : 'application/json', 'trainer_token' :'05b9f7ed87a1999a216b6b6ddefc49c8'}

TOKEN = '05b9f7ed87a1999a216b6b6ddefc49c8'

body = {
    "name": "Дэвгонг",
    "photo": "https://dolnikov.ru/pokemons/albums/087.png"
}

body2 = {
    "pokemon_id": "17073",
    "name": "Омастар",
    "photo": ""    
}

body3 = {
    "pokemon_id": "17073"
}

#создание покемона
response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body )
print(f'Статус код {response.status_code}.Сообщение:{response.text}')

#изменение имени покемона
response_change = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body2 )
print(f'Статус код {response_change.status_code}.Сообщение:{response_change.text}')

#поймать покемона в покебол
respons_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body3 )
print(f'Статус код {respons_pokeball.status_code}.Сообщение:{respons_pokeball.text}')