import requests
import  pprint


DOMAIN = 'https://api.hh.ru/'
url = 'https://api.hh.ru/vacancies '
url_vacancies = f'{DOMAIN}vacancies'

params = {
    'text': 'python developer AND NAME: (Python) AND (Django)',
    'page': 1
}
result = requests.get(url_vacancies, params=params).json()

# print(result.status_code)
# pprint.pprint(result.json())

# items = result ['items']
# first = items [0]
# pprint.pprint(first)
# print (first ['alternative_url'])
# one_vacancy_url = first ['url']