import requests
import pandas as pd

baseurl = "https://rickandmortyapi.com/api/"
endpoint = 'character'

def main_request(baseurl, endpoint, page):
    try:
        response = requests.get(f"{baseurl}{endpoint}?page={page}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed on page {page}: {e}")
        return None

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist = []
    for item in response['results']:
        charlist.append({
            'name': item['name'],
            'no_ep': len(item['episode']),
        })
    return charlist

if __name__ == "__main__":
    data = main_request(baseurl, endpoint, 1)
    if not data:
        exit()

    mainlist = []
    total_pages = get_pages(data)

    for page in range(1, total_pages + 1):
        response = main_request(baseurl, endpoint, page)
        if response:
            mainlist.extend(parse_json(response))

    df = pd.DataFrame(mainlist)
    df.to_csv('charlist.csv', index=False)
    print("Data saved to charlist.csv")
