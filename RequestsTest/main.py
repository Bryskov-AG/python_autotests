# Создание покемона (POST /pokemons )
# В ответе (терминале) должен прийти объект json
import requests

URL = 'https://api.pokemonbattle.ru/v2'    
TOKEN = 'USER_TOKEN'
HEADER= {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_createPokemons = {
    "name": "Бульбазавр",
    "photo_id": 1
}
# respons_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_createPokemons)
# print(respons_create.text)

# Смена имени покемона (PUT /pokemons )
# В ответе (терминале) должен прийти объект json

body_nameChange = {
    "pokemon_id": "157991",
    "name": "НьюЗаврик",
    "photo_id": 1
}

# respons_nameChange = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_nameChange)
# print(respons_nameChange.text)


# Поймать покемона в покебол (POST /trainers/add_pokeball )
# В ответе (терминале) должен прийти объект json

body_catchPokemon = {
    "pokemon_id": "157991"
}

respons_catchPokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catchPokemon)
print(respons_catchPokemon.text)