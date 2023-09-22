import random as r

"""
    Uses random in within a range of two numbers to generate a one or two, and print the corresponding message.
"""

def coin_flip():
    rand_num = r.randint(1, 2)
    if rand_num == 1:
        print("Heads!")
    else:
        print("Tails!")

coin_flip()
