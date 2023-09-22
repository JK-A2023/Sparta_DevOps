"""
    Takes file json file name from user, uses f string to put turn this into a parsed json dictionary.
    Then, uses a key, value loop to loop through all items, and prints out keys / values.
"""

import json

user_file = input("Enter the json file name here").strip()
parsed_json = json.loads(open(f'{user_file}.json').read())

for key, value in parsed_json.items():
    print(f"The key and value are ({key} : {value})")
