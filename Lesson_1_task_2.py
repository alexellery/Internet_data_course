import requests
import json
from pprint import pprint

main_link = 'https://ru.api.riotgames.com'
section = '/lol/league/v4/challengerleagues/by-queue/'
queue = 'RANKED_SOLO_5x5'

params = {'api_key': 'RGAPI-1fb63c7d-1586-4c63-831f-8b2f0f762ae3'}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
           "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8"
           }

response = requests.get(main_link + section + queue, headers=headers, params=params)

with open('lolets.json', 'w') as nvm:
    json.dump(response.json(), nvm)

data = response.json()

pprint(data)

