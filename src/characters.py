import requests

baseurl = "https://rickandmortyapi.com/api/"
endpoint = 'character'

def main_request(baseurl, endpoint):
    result = requests.get(baseurl + endpoint)
    return result.json()

def get_pages(response):
    pages = response['info']['pages']
    return pages

def parse_json(response):
    for item in response['results']:
        print(item['name'], len(item['episode']))
    return
    

data = main_request(baseurl, endpoint)
get_pages(data)
parse_json(data)
