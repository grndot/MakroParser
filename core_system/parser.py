import requests

per_page = 1000
page = 1

url = f'http://api.worldbank.org/v2/indicator?format=json&per_page={per_page}&page={page}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    total_pages = data[0]['pages']  # Общее количество страниц с индикаторами
    indicators = data[1]  # Список индикаторов на текущей странице

    for indicator in indicators:
        indicator_code = indicator['id']
        indicator_name = indicator['name']
        print(f'{indicator_code}: {indicator_name}')

    # Если есть другие страницы, повторите запрос для каждой страницы
    for page in range(2, total_pages + 1):
        url = f'http://api.worldbank.org/v2/indicator?format=json&per_page={per_page}&page={page}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            indicators = data[1]
            for indicator in indicators:
                indicator_code = indicator['id']
                indicator_name = indicator['name']
                print(f'{indicator_code}: {indicator_name}')
        else:
            print(f'Ошибка запроса на странице {page}: {response.status_code}')
else:
    print(f'Ошибка запроса: {response.status_code}')

