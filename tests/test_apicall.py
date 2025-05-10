import requests
import pandas as pd

baseurl = "https://rickandmortyapi.com/api/"
endpoint = 'character'

def main_request(baseurl, endpoint, x):
    result = requests.get(baseurl + endpoint + f'?page={x}')
    return result.json()

def get_pages(response):
    pages = response['info']['pages']
    return pages

def parse_json(response):
    charlist = []
    for item in response['results']:
        character = {
            'name': item['name'], 
            'no_ep': len(item['episode']),
        }

        charlist.append(character)
    return charlist


data = main_request(baseurl, endpoint, 1)

mainlist = []
for x in range (1,get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))

df = pd.DataFrame(mainlist)

#print(df.head(), df.tail())

df.to_csv('charlist.csv', index=False)