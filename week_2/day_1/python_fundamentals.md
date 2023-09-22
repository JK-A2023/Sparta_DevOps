# Variables

```python
"""
    String - Wrapped in quotes.
    Int - Whole numbers.
    Float - Decimal numbers.
    Boolean - Binary True / False
    Complex - 
"""

a = "Hello World" # String
b = 1 # Int
c = 1.5 # Float
d = False # Boolean
```

# Hello World Program

```python
"""
    Using print
"""

print("Hello World") # prints "Hello World" in the terminal.
```

# Using Input

```python
"""
    Using input
    Can take input from the user in the terminal and store this within a variable.
"""

print("Enter your name")
x = input()
print("Hello, " + x) # prints "Hello, <inputted-name>"
```

# String Slicing

```python
"""
    Using string manipulation to create specific sections of a string.
"""

hw = "Hello World!"
print(hw[0]) # prints "H"
print(hw[-1]) # prints "!"
print(hw[5:]) # prints everything after the 5th index: " World!"
print(hw[0:5]) # prints everything from the 0th index up to the 5th (excluding 5th): "Hello"
```

# String Methods
```python
"""
    String Methods are pre-built language methods to manipulate strings.
    
    Some examples are:
    
    strip() - removes whitespace
    len() - length
    count() - counts the set of arguments in a string
    lower() - Turns characters into lowercase
    capitalize() - capitalise the first letter
    replace() - replaces specified argument with new argument.
"""

example_text = "Hello, with this is a sentence"

print(example_text.count("e"))
print(example_text.lower())
print(example_text.capitalize())
print(example_text.replace("with", ","))
```

# Casting

```python
"""
    Essentially forcing one variable type to appear as another.
"""
a = 1
b = 2.5
c = "3"

print(a + b + int(c)) # prints 6.5 as
```

# Formatted Strings
```python
"""
    f-strings - being able to input variables into strings without the use of concatination. Does, however, leave 
    the string open to SQL injection.
"""
name = "Lassie"
years = 7
height_cm = 60.2

print(f"{name} is {years} old and {height_cm}cm tall")
# prints "Lassie is 7 years old and 60.2cm tall

snoop = "Snoopy"
snoop_years = 52

print(f"{snoop.upper()} is {years * 7} years old in dog years")
# prints "Snoopy is 42 years old in dog years"

pi = 3.14159265359

print(f"Pi to 3 decimal places: {pi:.3f}")
#prints 3.142

score = 16
max_score = 26

print(f"You scored {score/max_score}") # prints "You scored 0.6153846153846154"
print(f"You scored {score/max_score:%}") # prints "You scored 61.538462%"
print(f"You scored {score/max_score:.2%}") # prints "You scored 61.54%"
print(f"You scored {score/max_score:.0%}") # prints "You scored 62%"
```

# Booleans

```python
"""
    Booleans are binary positions between True or False.
"""
x = 0
y = 10

print(bool(x)) # inherently false
print(bool(y)) # y = 10, and so this is true. 
# Any number that is not 0 is true.
```

# Lists
```python
"""
    Lists (arrays in JavaScript). Are mutable.
"""
shopping_list = ["Salad", "Eggs", "Doughnuts", "Milk", "Salmon" ]
print(shopping_list)
# ['Salad', 'Eggs', 'Doughnuts', 'Milk', 'Salmon']

shopping_list[2] = "Tomato"
print(shopping_list)
# ['Salad', 'Eggs', 'Tomato', 'Milk', 'Salmon']

shopping_list.append("Carrots")
print(shopping_list)
# ['Salad', 'Eggs', 'Tomato', 'Milk', 'Salmon', 'Carrots']

shopping_list.extend(["Water", "Celery"])
print(shopping_list)
# ['Salad', 'Eggs', 'Tomato', 'Milk', 'Salmon', 'Carrots', 'Water', 'Celery']

shopping_list.remove("Water")
print(shopping_list)
# ['Salad', 'Eggs', 'Tomato', 'Milk', 'Salmon', 'Carrots', 'Celery']

shopping_list.pop()
print(shopping_list)
# ['Salad', 'Eggs', 'Tomato', 'Milk', 'Salmon', 'Carrots']

"""
    List slicing
"""

mixture = [1, 2, 3.0, "four", "five", "six"]
print(mixture)

print(mixture[1:3])
print(mixture[::-1])
```

# Tuples

```python
"""
    Tuples - Immutable, they cannot be changed
"""

essentials = ("bread", "eggs", "milk")

print(essentials)
print(type(essentials))
```

# Dictionaries

```python
"""
    Unordered Key/Value pairs. Mutable.   
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colours": ["Blue", "Red", "Black", "White"]
}

print(thisdict["brand"]) #prints "Ford"
print(thisdict["colours"][0]) #prints "Blue"

thisdict["brand"] = "Citroen" # changes the brand to "Citroen"
```