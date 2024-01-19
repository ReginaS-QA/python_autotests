import requests

"""
Pokemons test API
"""
URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': 'Ваш токен'
}

body = {
    "name": "Jill",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
}
response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER)
print(f'{response.json()}')

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': 'Ваш токен'
}
body = {
    "pokemon_id": "27886",
    "name": "Jack",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
}
response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER)
print(f'{response.json()}')

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': 'Ваш токен'
}
body = {
    "pokemon_id": "27886"
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER)
print(f'{response.json()}')