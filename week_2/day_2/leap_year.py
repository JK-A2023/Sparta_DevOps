"""
    Works out if a year is a leap year or not.
"""

print("Please enter a year")
user_year = int(input())

# if user_year % 100 == 0:
#     if user_year % 400 == 0:
#         print(f"The year {user_year} is a leap year.")
#     else:
#         print(f"The year {user_year} is not a leap year.")
# elif user_year % 4 == 0:
#     print(f"The year {user_year} is a leap year.")
# else:
#     print(f"The year {user_year} is not a leap year.")


if user_year % 4 == 0:
    if user_year % 100 == 0:
        if user_year % 400 == 0:
            print(f"The year {user_year} is a leap year.")
        else:
            print(f"The year {user_year} is not a leap year.")
    else:
        print(f"The year {user_year} is a leap year.")
else:
    print(f"The year {user_year} is not leap year.")