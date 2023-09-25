# Libraries and modules

Python has very extensive libraries and modules, this is great for DevOps engineers.

1. Module is a single file of functions, classes, variables, etc.
2. A library is a collection of modules.

```python
import math, random, requests
from pprint import pprint

num_float = 23.66

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)

rand_list = [1, 2, 3, 4, 5, 6, 7]
print(random.choice(rand_list))

rand_num = random.randint(1, 10)
print(rand_num)
#
request_bbc = requests.get("https://www.bbc.co.uk")

print(request_bbc.status_code)
pprint(request_bbc.content)

pikachu_request = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pprint(pikachu_request.status_code)
pprint(pikachu_request.content)
```
