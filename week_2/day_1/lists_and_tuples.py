"""
    Collections can store multiple pieces of data inside

    Lists - Called arrays in other languages
"""

shopping_list = ["Salad", "Eggs", "Doughnuts", "Milk", "Salmon" ]
print(shopping_list)

shopping_list[2] = "Tomato"
print(shopping_list)

shopping_list.append("Carrots")
print(shopping_list)

shopping_list.extend(["Water", "Celery"])
print(shopping_list)

shopping_list.remove("Water")
print(shopping_list)

shopping_list.pop()
print(shopping_list)

"""
    List slicing
"""

mixture = [1, 2, 3.0, "four", "five", "six"]
print(mixture)

print(mixture[1:3])
print(mixture[::-1])

"""
    Tuples - Immutable, they cannot be changed
"""

essentials = ("bread", "eggs", "milk")

print(essentials)
print(type(essentials))

