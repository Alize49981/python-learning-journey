import math
print(math.sqrt(81))
from math import sqrt
print(sqrt(49))
import random
print(random.randint(1, 10))
import random
def generate_random_number():
    return random.randint(1, 100)
print("random number:", generate_random_number())
pip install requests
import requests
requests = requests.get("https://www.example.com")
print(response.text)

url = "https://httpbin.org/post"

data = {
    "username": "john",
    "password": "1234"
}

response = requests.post(url, json=data)
print(response.json())
