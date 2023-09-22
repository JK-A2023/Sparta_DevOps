# Control Flow

```python
"""
    Control Flow:
    Controls the flow of code. It makes decisions and ignores other parts of code depending on certain factors.
    Check if conditions are true before a piece of code is ran.
    "If a piece of code is true, then do this piece. If not, then do a different piece".

    elif - Less processing power, and runs only if the condition is met. If you use multiple if statements, multiple can
    run as more than one can be true at the same time.
"""

# IF STATEMENTS

"""
    Here, we are saying that the age limit variable is 18. Within the if block,
    if the age variable is greater than or equal to 18, then print "Please enter",
    else, print "You are too young to enter".
"""

print("How old are you?")
user_age = int(input())

age_limit = 18

if user_age >= age_limit:
    print("Please enter.")
else:
    print("You are too young to enter.")

# IF & ELIF STATEMENTS

"""
    Similar to above, this script takes in a rating from the user.
    IF the input is "u", the a print statement of "All age groups can watch"
    is printed to the console. 
    However, this script used elif, *else if*, to progressively check the input
    from the user. If at any point the user input matches the is equal to requirement,
    it will print the requisite print statement.
    Finally, there is a catch all if the user input matches none of the if statements,
    calling for the user to only input valid ratings.
"""

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
```

# For loops


```python
"""
    For loops. Below are three data collections, a list, an embedded list,
    and a dictionary.
"""
```
![img_1.png](img_1.png)
```python

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

for num in list_data:
    print(num * 2)

"""
    for X in Y:
        for Z in X:
        
    Embedded for loops seek to iterate through each index on the "1st" level, and then perform an operation on the 
    current "2nd" level embedded index, and then it moves onto the next 1st level index, and performs an operation on the
    current 2nd level index. This continues for the entire length of the list.
"""

for lists in embedded_lists:
    for num in lists:
        print(num)

"""
    Dictionary loops
    
    The .values() method looks through the values, not keys.
"""

for value in dict_data:
    print(value)

for item in dict_data.values():
    print(item)

for item in dict_data.values():
    for embed_value in item.keys():
        print(embed_value)
    for embed_value in item.values():
        print(embed_value)

"""
    get values for individual keys
"""

for items in dict_data.values():
    print(items["name"])

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
        
```

# While loops
```python
"""
    While loops

    For loops are all to do with iterating through a collection.
    While loops are more like a monitor, while something remains true, continue to do XYZ.
"""
```
![img_2.png](img_2.png)
```python

x = 0

# Simple use of incremented x until it reaches 20, upon which the "while"
# criteria will no longer be true, and cease iterating.

while x < 20:
    x += 1
    print(x)

while x < 10:
    print(f"It's working --> {x}")
    if x == 4:
        break
    x += 1
    
"""
    Using user prompts in the terminal. 
    If the inputted age is not a number, the user_prompt remains true,
    looping the "while" loop. When the user gives an answer that is
    a digit, the user_prompt is no longer true.
"""

user_prompt = True

while user_prompt:
    age = input("What is your age?").strip()
    if age.isdigit() and int(age) < 110:
        user_prompt = False
        print(f"Your age is {age}")
    else:
        print("Please provide your answer in digits, and below 110")

```

