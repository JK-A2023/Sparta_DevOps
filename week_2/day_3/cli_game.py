"""
    Unfinished - was not able to get a round-system working in time. Currently, one round is able to be fulfilled, with
    the user being able to select a user, and choose to use their special ability, affecting the health of the CPU
    character.
"""

import random as r

def character_select():
    character_specs = {
        "BigBoi": {
            "Health": 100,
            "Strength": 5,
            "Armour": 1,
            "Power": "Smash",
            "Crit Chance": 0
        },
        "Frog": {
            "Health": 25,
            "Strength": 50,
            "Armour": 2,
            "Power": "Frog",
            "Crit Chance": 75
        },
        "Guh": {
            "Health": 10,
            "Strength": 25,
            "Armour": 3,
            "Power": "Slap",
            "Crit Chance": 25
        }
    }
    characters = ["BigBoi", "Frog", "Guh"]

    game_time = True

    while game_time:

        character_select_one = True
        selected_character_one = None
        selected_character_two = None

        while character_select_one:
            print(characters)
            user_characters_choice = input("Player One, choose your character!")

            if user_characters_choice not in characters:
                print("Please select a valid character")
                continue

            if user_characters_choice in characters:
                character_confirmation = input(f"You have selected {user_characters_choice}. Is this correct (Yes/No)?")
                if character_confirmation == "Yes":
                    print("Character confirmed")
                    game_time = False
                    character_select_one = False
                    selected_character_one = user_characters_choice

                elif character_confirmation == "No":
                    print("Selection cancelled")
                    continue

                else:
                    print("Please enter a valid answer")
                    continue

        CPU_or_player_2 = input("Is there a player two (Yes/No)?")
        if CPU_or_player_2 == "Yes":
            character_select_two = True

            while character_select_two:
                print(characters)
                user_characters_choice = input("Player Two, choose your character!")

                if user_characters_choice not in characters:
                    print("Please select a valid character")
                    continue

                if user_characters_choice in characters:
                    character_confirmation = input(
                        f"You have selected {user_characters_choice}. Is this correct (Yes/No)?")
                    if character_confirmation == "Yes":
                        print("Character confirmed")
                        game_time = False
                        character_select_two = False
                        selected_character_two = user_characters_choice

                    elif character_confirmation == "No":
                        print("Selection cancelled")
                        continue

                    else:
                        print("Please enter a valid answer")
                        continue

        else:
            cpu_use = True

            while cpu_use:
                cpu_character = r.choice(characters)
                selected_character_two = cpu_character
                print(f"The CPU has picked {cpu_character}!")
                break

        print(f"Time for {selected_character_one} and {selected_character_two} to fight!!")

        time_to_fight = True

        while time_to_fight:
            first_round = True
            player_one_power = character_specs[selected_character_one]["Power"]
            player_one_crit_chance = character_specs[selected_character_one]["Crit Chance"]
            player_one_strength = character_specs[selected_character_one]["Strength"]
            player_one_health = character_specs[selected_character_one]["Health"]

            player_two_power = character_specs[selected_character_two]["Power"]
            player_two_crit_chance = character_specs[selected_character_two]["Crit Chance"]
            player_two_strength = character_specs[selected_character_two]["Strength"]
            player_two_health = character_specs[selected_character_two]["Health"]

            while first_round:
                print(f"Player One's {selected_character_one} one goes first!")

                player_one_move = input(f"Use {selected_character_one}'s power {player_one_power} (Yes/No)?")

                if player_one_move == "Yes":
                    player_one_crit = (player_one_strength * player_one_crit_chance) / 100
                    print(f"Player One's {selected_character_one} has hit Player Two's {selected_character_two} for {player_one_crit}!!")
                    player_two_health = character_specs[selected_character_two]["Health"] - player_one_crit

                    if player_two_health <= 0:
                        print(f"Player Two's {selected_character_two}'s health has fallen below 0!")
                        first_round = False

                    else:
                        print("Time for Player Two's turn!")
                        first_round = False

                elif player_one_move == "No":
                    print("mate wyd???")
                    continue

                else:
                    print("Please choose Yes or No")
                    continue

                if player_two_health > 0:
                    player_two_crit = (player_two_strength * player_two_crit_chance) / 100
                    print(f"Player Two's {selected_character_two} has hit Player One's {selected_character_one} for {player_two_crit}!!")
                    player_one_health = character_specs[selected_character_one]["Health"] - player_two_crit

                    if player_one_health <= 0:
                        print(f"Player One's {selected_character_one}'s health has fallen below 0!")
                        time_to_fight = False

                    else:
                        print("Time for Player Two's turn!")
                        first_round = False

            if player_one_health <= 0:
                print("Player Two wins!")
                break

            if player_two_health <= 0:
                print("Player One wins!")
                break

            print(f"Player Two's's {selected_character_two} goes second!")

            break

        print("The fight has concluded")
        break

def fighting_game(characters):
    return characters

fighting_game(character_select())