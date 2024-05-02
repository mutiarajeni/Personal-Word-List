import requests

api_key = '1a535167-8226-43ee-aa8a-5428de258a78'
word = 'voluminous'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)
definitions = res.json()

for definition in definitions:
    print(definition)