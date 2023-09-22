"""
    For Loops
"""

list_data = [1, 2, 3, 4, 5]

embedded_lists = [[1, 2, 3], [4, 5, 6]]

dict_data = {
    1: {"name": "Bronson",
        "money": "£0.05"},
    2: {"name": "Masha",
        "money": "£3.66"},
    3: {"name": "Roscie",
        "money": "£1.14"},
}

"""
    for X in Y:
    This type of loop iterates through each index within the list.
    It will then perform the function upon each item in the list.
"""

# for num in list_data:
#     print(num * 2)

"""
    for X in Y:
        for Z in X:

    Embedded for loops seek to iterate through each index on the "1st" level, and then perform an operation on the 
    current "2nd" level embedded index, and then it moves onto the next 1st level index, and performs an operation on the
    current 2nd level index. This continues for the entire length of the list.
"""

# for lists in embedded_lists:
#     for num in lists:
#         print(num)

"""
    Dictionary loops

    The .values() method looks through the values, not keys.
"""

# for value in dict_data:
#     print(value)

# for item in dict_data.values():
#     print(item)

# for item in dict_data.values():
#     for embed_value in item.keys():
#         print(embed_value)
#     for embed_value in item.values():
#         print(embed_value)

"""
    get values for individual keys
"""

# for items in dict_data.values():
#     print(items["name"])

"""
    loops and if statements
"""

for num in list_data:
    if num == 3:
        print("I found 3!")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon!")
