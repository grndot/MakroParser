import requests
import pandas as pd

per_page = 1000
page = 1

url = f'http://api.worldbank.org/v2/indicator?format=json&per_page={per_page}&page={page}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    total_pages = data[0]['pages']  # Общее количество страниц с индикаторами

    indicators = {}

    for indicator in data[1]:
        indicator_code = indicator['id']
        indicator_name = indicator['name']
        indicators[indicator_code] = indicator_name

    # Если есть другие страницы, повторите запрос для каждой страницы
    for page in range(2, total_pages + 1):
        url = f'http://api.worldbank.org/v2/indicator?format=json&per_page={per_page}&page={page}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for indicator in data[1]:
                indicator_code = indicator['id']
                indicator_name = indicator['name']
                indicators[indicator_code] = indicator_name
        else:
            print(f'Ошибка запроса на странице {page}: {response.status_code}')

    # Создаем pandas Series с индикаторами и сохраняем его в файл CSV
    indicators_series = pd.Series(indicators)
    indicators_series.to_csv('indicators.csv', header=['Indicator Name'])

else:
    print(f'Ошибка запроса: {response.status_code}')
