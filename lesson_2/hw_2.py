# Вариант 1
# Необходимо собрать информацию о вакансиях на вводимую должность
# (используем input или через аргументы получаем должность)
# с сайтов HH(обязательно) и/или Superjob(по желанию).
# Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы).
# Получившийся список должен содержать в себе минимум:
# Наименование вакансии.
# Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта.цифры преобразуем к цифрам).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия.
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
# Структура должна быть одинаковая для вакансий с обоих сайтов.
# Общий результат можно вывести с помощью dataFrame через pandas.
# Сохраните в json либо csv.

# https://hh.ru/search/vacancy ? clusters=true & ored_clusters=true & enable_snippets=true & salary= & text=python


import requests
from bs4 import BeautifulSoup as bs
import json
from pprint import pprint

my_vacancy = input("Введите наименование вакасансии: ")

url ='https://hh.ru'
params = {'clusters' : 'true',
           'ored_clusters': 'true',
          'enable_snippets': 'true',
          'salary': None,
          'text': my_vacancy,
          'page': 0}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

response = requests.get(url+'/search/vacancy', params=params, headers=headers)
dom = bs(response.text, 'html.parser')

vacancy_list = []
while params['page'] < 5:
    response = requests.get(url + '/search/vacancy', params=params, headers=headers)
    dom = bs(response.text, 'html.parser')
    vacants = dom.find_all('div', {'class': 'vacancy-serp-item'})

    if response.ok and vacants:

        for vacancy in vacants:
            vacancy_data = {}
            info = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
            name = info.text
            link = info['href']
            site = url
            try:
                salary = vacancy.find('div', {'class': 'vacancy-serp-item__sidebar'}).text
                spl = salary.split()
                if '–' in salary:
                    salary_min = int(spl[0]+spl[1])
                    salary_max = int(spl[3]+spl[4])
                    salary_cur = spl[5]
                elif 'от' in salary:
                    salary_min = int(spl[1] + spl[2])
                    salary_max = None
                    salary_cur = spl[3]
                elif 'до' in salary:
                    salary_min = None
                    salary_max = int(spl[1] + spl[2])
                    salary_cur = spl[3]
                else:
                    salary_min = int(spl[0] + spl[1])
                    salary_max = int(spl[0] + spl[1])
                    salary_cur = spl[2]
            except:
                salary = None

            vacancy_data['name'] = name
            vacancy_data['link'] = link
            vacancy_data['site'] = site
            vacancy_data['salary_min'] = salary_min
            vacancy_data['salary_max'] = salary_max
            vacancy_data['salary_cur'] = salary_cur
            vacancy_list.append(vacancy_data)
        print(f"обработана {params['page']+1} страница")
        params['page'] += 1
    else:
        break
pprint(vacancy_list)


# with open('vacancy_list.json','w', encoding= 'UTF-8') as file:
#     json.dump(vacancy_list, file)


