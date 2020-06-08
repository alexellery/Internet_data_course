import requests
import json
from pprint import pprint

main_link = 'https://api.github.com'
username = 'alexellery'

response = requests.get(f'{main_link}/users/{username}/repos')

print(type(response))

with open('data.json', 'w') as data:
    json.dump(response.json(), data)

for i in response.json():
    pprint(f'У пользователя {username} есть репозиторий {i["name"]}')






