import requests, json, random
from pprint import pprint


"""
    Generates a response of all of the data from the Poke api, and returns it in json format.
"""
def poke_response_init():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=1281'
    response = requests.get(url)
    all_pokemon_data = response.json()
    return all_pokemon_data


"""
    Loops through all of the pokemon data and generates a list of names.
"""
def all_poke_names(all_pokemon_data):
    poke_names = [pokemon["name"] for pokemon in all_pokemon_data["results"]]
    return poke_names


"""
    Input from the user for a Pokemon name. If the input is found within the list of names, the use can confirm or reset
    the choosing process. If the user enters a name that is not within the list, they are told to select from available
    names, and resets to the start.
"""
def user_poke_init(all_poke_names_from_list):
    character_input = input("Choose your Pokemon!").lower()
    character_select = True
    while character_select:
        if character_input in all_poke_names_from_list:
            character_confirmation = input(f"Do you want to continue with {character_input.capitalize()} ?")
            if character_confirmation == "Yes".lower():
                return character_input
            elif character_confirmation == "No".lower():
                character_select = False
                new_response = poke_response_init()
                new_set_of_names = all_poke_names(new_response)
                return user_poke_init(new_set_of_names)
            else:
                print("Please specify 'Yes' or 'No'.")
        else:
            print(f"Please choose a Pokemon. {character_input.capitalize()} is not a Pokemon!")
            character_select = False
            new_response = poke_response_init()
            new_set_of_names = all_poke_names(new_response)
            return user_poke_init(new_set_of_names)


"""
    Pulls in all previous functions. If the user_input name is found within the list of names, a new response is made to
    to generate a url of the specifically named Pokemon.
"""
def user_poke_setup(poke_data, poke_names, poke_init):
    if poke_init in poke_names:
        print(f"We found {poke_init.capitalize()}!")
        for result in poke_data["results"]:
            if result['name'] == poke_init:
                pokemon_url = result['url']
                user_poke_response = requests.get(pokemon_url)
                pokemon_data = user_poke_response.json()
                return pokemon_data


"""
    Using the users set up data, we bring in the pokemons stats
"""
def user_poke_stats(poke_setup, poke_name):
    print(f"Your {poke_name.capitalize()} is being set up!")
    pokemon_data_stats = []
    for key in poke_setup.keys():
        pokemon_data_stats.append(key)
    print(pokemon_data_stats)


def game():

    pokemon_data = poke_response_init()
    poke_names = all_poke_names(pokemon_data)
    poke_name = user_poke_init(poke_names)
    poke_setup = user_poke_setup(poke_response_init(), poke_names, poke_name)
    user_poke_stats(poke_setup, poke_name)

game()
