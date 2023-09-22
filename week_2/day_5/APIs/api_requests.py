"""
    Api Requests
"""

import requests, json
from pprint import pprint

post_code_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

# Long way
# post_codes = json.loads(post_code_req)

#Short way

pprint(post_code_req.json())

# print(post_codes)

# pprint(post_code_req.status_code)
# pprint(post_code_req.headers)
# pprint(post_code_req.content)

