import requests

url = 'https://www.google.ru'

response = requests.get(url)
response.headers.get('Content-Type')
response.text #текстовое содержимое html-код
response.content #бинарное содержимое
response.encoding #выдернуть кодировку,можем принудительно перекодировать response.content.decode('utf-8')
if response.status_code == 200:
    pass
if response.ok:
    pass


print()