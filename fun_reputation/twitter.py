import requests
import urllib.parse

print(urllib.parse.quote("지드래곤"))

url = ''
response = requests.get(url, headers=headers)
print(response.json())

for x in response.json()['data']['search_timeline'][]

