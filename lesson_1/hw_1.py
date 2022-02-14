import requests
import json
from pprint import pprint

repos_url = 'https://api.github.com'

user_name = 'Olga-geek' #input("Enter the github user_name:")
response = requests.get(f'{repos_url}/users/{user_name}/repos')

j_data = response.json()
with open('data.txt', 'w') as j_file:
    json.dump(j_data, j_file)

# pprint(j_data)
num=1
for i in j_data:
    print(f"{num} наименование репозитория {i['name']}")
    num+=1




