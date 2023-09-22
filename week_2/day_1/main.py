"""
    User input
    Need some examples for input
"""

# Example

# print("Enter your name")
# x = input()
# print("Hello, " + x)

# ###############################################################################################################################################

"""
    Numeric Types of int, float, complex

    What is complex?
"""

# ###############################################################################################################################################

"""
    String Slicing
"""

# hw = "Hello World!"
#
# print(hw[-6:])

# ###############################################################################################################################################

"""
    String Methods

    strip() - removes whitespace
    len() - length
    count() - counts the set of arguments in a string
    lower() - Turns characters into lowercase
    capitalize() - capitalise the first letter
    replace() - replaces specified argument with new argument.
"""

# example_text = "Hello, with this is a sentence"

# print(example_text.count("e"))
# print(example_text.lower())
# print(example_text.capitalize())
# print(example_text.replace("with", ","))

# ###############################################################################################################################################

"""
    Casting
"""

a = 1
b = 2.5
c = "3"
#
print(a + b + int(c))

# ###############################################################################################################################################

"""
    formatted-strings
    f-strings
"""

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} old and {height_cm} tall")
#
# snoop = "Snoopy"
# snoop_years = 52
#
# print(f"{snoop.upper()} is {years * 7} old in dog years")
#
# pi = 3.14159265359
#
# print(f"Pi to 3 decimal places: {pi:.3f}")

# ###############################################################################################################################################

# weight = float(input("Enter your weight in KG: "))
# height = (float(input("Enter your height in cm: ")) / 100)
# final_height = height ** 2
#
# bmi = weight / final_height
# print(bmi)


score = 16
max_score = 26

print(f"You scored {score / max_score}")
print(f"You scored {score / max_score:%}")
print(f"You scored {score / max_score:.2%}")
print(f"You scored {score / max_score:.0%}")