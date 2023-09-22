"""
    Takes in multiple
"""

number = int(input("Enter a number!").strip())

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz!")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("That is not a multiple of 3 or 5!")

