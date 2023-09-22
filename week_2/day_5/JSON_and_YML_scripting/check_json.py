"""
    checks if there is at least one command line argument. If there is, check if the file specified exists.
    If it does, read it, and print that it is valid. Else not found. If there are no arguments, specify the usage.
"""

import json, os, sys

if len(sys.argv) == 2:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], 'r')
        json.load(file)
        file.close()
        print("JSON is VALID!")
    else:
        print(sys.argv[1] + " not found")

else:
    print("Usage: check_json.py <file>")
