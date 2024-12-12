import requests

BASE_URL = 'http://127.0.0.1:8000/api/'
TOKEN = 'ea6a55e91db49c2f350d251befce9ec3ff03fafb'

def get_data(endpoint):
    headers = {'Authorization': f'Token {TOKEN}'}
    response = requests.get(f'{BASE_URL}{endpoint}', headers=headers)
    return response.json()

# Example Usage
if __name__ == '__main__':
    print(get_data('food-items/'))
