"""
    Scripting

    There are seven modules that we can consider "core" in Python.

"""

import sys, os, subprocess, math, random, datetime, json

"""
    Sys
"""

print(sys.version)

"""
     OS

     file and folder manipulation
"""

print(os.getcwd())

# os.mkdir("test_dir")


"""
    Subprocess
"""

subprocess.run(["python", "hello_world.py"])

"""
    Math
"""

pi = math.pi

pi_string = str(pi)

print(f"The value of pi is {pi_string}")

"""
    Random
"""

rand_num = random.randrange(1, 10)
print(rand_num)

"""
    Datetime    
"""

whatisthedate = datetime.datetime.now()
print(whatisthedate)

"""
    JSON
"""

x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

print(type(x))

y = json.dumps(x)
print(type(y))
