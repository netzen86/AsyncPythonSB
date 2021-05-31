import requests

r = requests.get('https://foodish-api.herokuapp.com/api/')
print(f"status code is {r.status_code}")
print(f"response is {r.json()}")