import requests
import json
from pprint import pprint

repos_url = 'https://api.github.com/users/Olga-geek/repos'

user_name = 'Olga-geek' #input("Enter the github user_name:")
response = requests.get(repos_url)

j_data = response.json()
with open('data.txt', 'w') as j_file:
    json.dump(j_data, j_file)

pprint(j_data)





