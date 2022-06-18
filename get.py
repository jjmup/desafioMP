import requests
import time
import json
response = requests.get('https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios')
print(response.url)
content = response.content
print(content)
time.sleep(15)
"""response_json = json.get('https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios')
print(response_json.url)
time.sleep(5)
content_json = response_json.content
print(content_json)
time.sleep(5)"""
