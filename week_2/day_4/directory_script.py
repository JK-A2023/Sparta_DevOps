"""
    Takes input from the user and creates a directory with that name.
"""
import os

user_directory_name = input("What do you want your directory to be called?")
user_directory_path = input("Where do you want the path to be?")
user_new_file = input("And finally, what would you like the file to be named?")

new_path = os.path.join(user_directory_path, user_directory_name)
new_file = os.path.join(new_path, user_new_file)

os.mkdir(new_path)
open(new_file, 'w')
