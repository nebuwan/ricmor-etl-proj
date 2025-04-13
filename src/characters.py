#https://www.youtube.com/watch?v=-oPuGc05Lxs

import requests

baseurl = "https://rickandmortyapi.com/api/"

endpoint = 'character'

result = requests.get(baseurl + endpoint)
data = result.json()

pages = data['info']['pages']

print(data['results'][0]['name'])
