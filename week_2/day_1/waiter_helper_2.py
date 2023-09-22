"""
    Waiter_helper is a script that takes in user input for their name, and provides various menus for the user to pick
    from. If the user provides an item that is within the menu's lists, the information is stored, else the script will
    restart. Ultimately, it provides a full list of items ordered, as well as the total cost in the form of a bill.
"""

starters = {
    "Patatas Fritas": "£3",
    "Menemen": "£5",
    "Eggs": "£2",
    "Toast": "£1.50"
}
mains = {
    "Fish and Chips": "£15",
    "Lancashire Cheese Pie": "£9",
    "Steak": "£16",
    "Salad": "£8"
}
desserts = {
    "Sundae": "£5",
    "Chocolate cake": "£6",
    "Cheese cake": "£5"
}
drinks = {
    "Water": "Free",
    "Juice": "£1.50",
    "Wine": "£6 per glass"
}

print("What is your name")
user_name = input()

print("Hello " + user_name + "!")
print("Please choose a starter: ")
print(starters)

starters_list = list(starters.keys())
user_starter = input()

if user_starter in starters_list:

    print("Please choose a main:")
    print(mains)
    mains_list = list(mains.keys())
    user_main = input()
    if user_main in mains_list:

        print("Please choose a dessert:")
        print(desserts)
        desserts_list = list(desserts.keys())
        user_dessert = input()
        if user_dessert in desserts_list:

            print("Please choose a drink:")
            print(drinks)
            drinks_list = list(drinks.keys())
            user_drink = input()
            if user_drink in drinks_list:

                print(f"Thank you {user_name}. Please review your order")
                print(user_starter + ", " + user_main + ",", user_dessert + ", " + user_drink)
                print("Are you happy with this order")
                user_response = input()
                if user_response == "Yes":

                    if "Water" in user_drink:
                        total_bill = (
                            float(starters[user_starter][1:])
                            + float(mains[user_main][1:])
                            + float(desserts[user_dessert][1:])
                        )
                        print("Great. We will bring that soon.")
                        print(f" Hi {user_name}, I hope you enjoyed the meal. Here is the bill: ")
                        print(f"Starter: {user_starter} - {starters[user_starter]}")
                        print(f"Main: {user_main} - {mains[user_main]}")
                        print(f"Dessert: {user_dessert} - {desserts[user_dessert]}")
                        print(f"Drink: {user_drink} - {drinks[user_drink]}")
                        print(f"Total: £{total_bill}")
                    else:
                        total_bill = (
                            float(starters[user_starter][1:])
                            + float(mains[user_main][1:])
                            + float(desserts[user_dessert][1:])
                            + float(drinks[user_drink][1:3])
                        )
                        print("Great. We will bring that soon.")
                        print(f" Hi {user_name}, I hope you enjoyed the meal. Here is the bill: ")
                        print(f"Starter: {user_starter} - {starters[user_starter]}")
                        print(f"Main: {user_main} - {mains[user_main]}")
                        print(f"Dessert: {user_dessert} - {desserts[user_dessert]}")
                        print(f"Drink: {user_drink} - {drinks[user_drink]}")
                        print(f"Total: £{total_bill}")

                elif user_response == "No":
                    print("Sorry, please order again.")

                else:
                    print("What?")
            else:
                print("That is not a drink, try again.")
        else:
            print("That is not a dessert, try again.")
    else:
        print("That is not a main, try again.")
else:
    print("That is not a starter, try again.")
