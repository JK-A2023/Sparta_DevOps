"""
    Takes a user number. If the number modulo 2 leaves no remainder, it must be even. Else, it is odd.
    After this calculation, it prints out the following print statement.
"""

user_number = input("Please enter a number")

if float(user_number) % 1 != 0:

    split_number = [*user_number]
    print(split_number)
    if int(split_number[-1]) >= 5:
        print("Your number has been rounded up")
        whole_number = int("".join(split_number))
        print(whole_number)
        # if whole_number % 2 == 0:
        #     print(f"{whole_number} is even")
        # else:
        #     print(f"{whole_number} is odd")
# else:
#     if int(user_number) % 2 == 0:
#         print(f"{user_number} is even")
#     else:
#         print(f"{user_number} is odd")
