import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': 'Ваш токен'
}

def test_get_trainers():
    """
    PT-1. Get trainers status code
    """
    response = requests.get(url=f'{URL}/trainers', params={"level": 2}, headers=HEADER)
    assert response.status_code == 200, "Unexpected status code"
    print(f'{response.json()}')

def test_get_trainer_name():
    """
    PT-2. Get your trainer's name
    """
    response = requests.get(url=f'{URL}/trainers', params={"trainer_id": 3614}, headers=HEADER)
    assert response.json()["trainer_name"] == "Jessie", 'Unexpected name'
    print(f'{response.json()}')