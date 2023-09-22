"""
Echoing to the terminal
"""

import os

user_string = input("Tell me what you want me to say!")

os.system(f'echo {user_string}')