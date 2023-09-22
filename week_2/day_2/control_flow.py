"""
    Control Flow:
    Controls the flow of code. It makes decisions and ignores other parts of code depending on certain factors.
    Check if conditions are true before a piece of code is ran.
    "If a piece of code is true, then do this piece. If not, then do a different piece".

    elif - Less processing power, and runs only if the condition is met. If you use multiple if statements, multiple can
    run as more than one can be true at the same time.
"""

# IF STATEMENTS

print("How old are you?")
user_age = int(input())

age_limit = 18

if user_age >= age_limit:
    print("Please enter.")
else:
    print("You are too young to enter.")

# IF & ELIF STATEMENTS

print("Please enter film rating:")
film_rating = input()

if film_rating.lower() == "u":
    print("All age groups can watch")
elif film_rating.lower() == "pg":
    print("Parental guidance is advised for this movie")
elif film_rating.lower() == "12" or film_rating.lower() == "12a":
    print("People over the age of 12 can watch this movie")
elif film_rating.lower() == "15":
    print("People over the age of 15 can watch this movie")
elif film_rating.lower() == "18":
    print("People over the age of 18 can watch this movie")
else:
    print("This is not a valid rating, please use 'u', 'pg', '12' or '12', '15', '18'")

