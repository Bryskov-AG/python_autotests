import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'    
TOKEN = 'USER_TOKEN'
HEADER= {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '6932'

# Проверь, что ответ запрос GET /trainers приходит с кодом 200
def test_status_code():
    response = requests.get(url =f'{URL}/trainers')
    assert response.status_code == 200

# Проверь, что в ответе приходит строчка с именем твоего тренера
# (Не забудь прописать в квери id твоего тренера (​​​​trainer_id​​​​))

def test_trainer_name():
    response = requests.get(url =f'{URL}/trainers',params = {'trainer_id' : TRAINER_ID})
    assert response.json()["data"][0]['trainer_name'] == 'Santei'