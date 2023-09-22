"""
    Functions

    DRY - Don't repeat yourself.
    Avoid repeating yourself, highly inefficient code, leads to bugs, as well as spaghetti-fied code that becomes hard
    to read.
    Instead, use function to reference previous code.
"""


# Making a function:


def print_something():
    print("Something")


# print_something()


def print_another_thing(print_string):
    print(print_string)


# print_another_thing(input("What should be printed??"))


def greeting(name):
    print(f"Hello, my name is {name}")


# greeting("Andrew")


"""
    The Return Statement - holds a value. All it does is hold the value resulting from a function. This value can be
    used later.

    Default arguments. Using int1=2, int2=2 means that if the function is called with no arguments, it will default 
    to these values.
"""


def addition(int1=2, int2=2):
    return int1 + int2


addition(2, 2)

"""
    Variable argument amounts - use the wildcard operator <*> before the arguments.
    Multi-arguments are in tuples.
    If putting in more arguments, put them before the multi arg.
"""


def multi_args_one(*multiargs):
    for arg in multiargs:
        print(arg * 2)


multi_args_one(1, 2, 3, 4, 5)


def multi_args_two(arg2, *multiargs):
    for arg in multiargs:
        print(arg * 2)
    print(arg2)


multi_args_two(1, 2, 3, 4, 5)

"""
    Type hints - give your IDE an idea of what data types to expect.
"""

"""
    Good practices in functions:
        Add useful doc strings.
        Clear function names and argument names.
"""
