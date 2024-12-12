import requests

headers = {
    'Authorization': 'Token ea6a55e91db49c2f350d251befce9ec3ff03fafb',
}
response = requests.get('http://127.0.0.1:8000/api/food-items/', headers=headers)
print(response.json())
