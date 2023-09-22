"""
    While loops

    For loops are all to do with iterating through a collection.
    While loops are more like a monitor, while something remains true, continue to do XYZ.
"""

# x = 0

# while x < 20:
#     x += 1
#     print(x)
#
# while x < 10:
#     print(f"It's working --> {x}")
#     if x == 4:
#         break
#     x += 1

user_prompt = True

while user_prompt:
    age = input("What is your age?").strip()
    if age.isdigit() and int(age) < 110:
        user_prompt = False
        print(f"Your age is {age}")
    else:
        print("Please provide your answer in digits, and below 110")
