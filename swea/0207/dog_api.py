import requests
import pprint

URL = 'https://dog.ceo/api/breeds/image/random'
response = requests.get(URL).json()
print(pprint.pprint(response))