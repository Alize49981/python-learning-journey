
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code)
print(response.json())
data = response.json()
url = "https://httpbin.org/post"

data = {
    "username": "Alih",
    "password": "1234"
}

response = requests.post(url, json=data)
print(response.json())
