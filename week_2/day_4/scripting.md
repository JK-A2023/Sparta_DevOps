# Scripting

There are seven modules that we can consider "core" in Python.

```python
import sys, os, subprocess, math, random, datetime, json
```

## Sys

```python
import sys

print(sys.version)
```

Prints current version of PyCharm.

## Os

```python
import os

print(os.getcwd())

os.mkdir("test_dir")
```
1. gets current directory.
2. creates directory called "test_dir"

## Subprocess

```python
import subprocess

subprocess.run(["python", "hello_world.py"])
```
Can run other files, just requires language and files name.

## Math

```python
import math

pi = math.pi

pi_string = str(pi)

print(f"The value of pi is {pi_string}")
```

Math stuff.

## Random

```python
import random

rand_num = random.randrange(1,10)
print(rand_num)
```

Random stuff.

## Datetime

```python
import datetime

whatisthedate = datetime.datetime.now()
print(whatisthedate)
```

Prints many date functionalities.

## JSON

```python

import json
x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

print(type(x))

y = json.dumps(x)
print(type(y))
```

Imports many JSON functionalities.


