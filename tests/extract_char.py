import requests
import pandas as pd
from pathlib import Path

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

def extract_characters():
    baseurl = "https://rickandmortyapi.com/api/"
    endpoint = 'character'
    data = main_request(baseurl, endpoint, 1)
    if not data:
        return

    all_chars = []
    total_pages = get_pages(data)
    for page in range(1, total_pages + 1):
        response = main_request(baseurl, endpoint, page)
        if response:
            all_chars.extend(parse_json(response))

    df = pd.DataFrame(all_chars)
    Path("data").mkdir(exist_ok=True)
    df.to_csv("data/charlist.csv", index=False)
    print("Data saved to data/charlist.csv")

if __name__ == "__main__":
    extract_characters()