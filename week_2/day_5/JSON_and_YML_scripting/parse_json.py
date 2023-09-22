"""
    Parsing is making something (more) understandable.

    Loads turns json into a python dictionary
    load reads json.
"""

import json

parsed_json = json.loads(open('example_json.json').read())
value = parsed_json['name']

print(type(parsed_json))
print(value)
