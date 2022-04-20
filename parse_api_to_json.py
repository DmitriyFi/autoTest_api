import requests
import json
from configuration import SERVICE3_URL

api = SERVICE3_URL                                       # put your SERVICE_URL  here, imported from configuration file

response = requests.get(api).json()

with open('tests/my/api_response.json', 'w') as json_file:
    json.dump(response, json_file, indent=4)
