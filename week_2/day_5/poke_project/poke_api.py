import requests, json, random
from pprint import pprint

# Get the list of pokemon from the API


# def init_pokemon():
#     url = 'https://pokeapi.co/api/v2/pokemon?limit=1281'
#     response = requests.get(url)
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         poke_names = [pokemon["name"] for pokemon in pokemon_data["results"]]
#         cpu_name = random.choices(poke_names)
#         return cpu_name
#
# cpu_character = init_pokemon()[0]
# def cpu_attributes(cpu_char):
#     pass

url = 'https://pokeapi.co/api/v2/pokemon/1'
response = requests.get(url)
bulbasuar = json.loads(response.content)

# for key in bulbasuar:
#     print(key)


poke_stats = bulbasuar['stats']
pprint(poke_stats)

stat_names = [stat["stat"] for stat in poke_stats]
pprint(stat_names)

stat_name_final = [name["name"] for name in stat_names]
print(stat_name_final)



