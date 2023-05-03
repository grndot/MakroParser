import requests
import json
import pandas as pd

# Получаем список всех стран
def get_all_country_names():
    countries_url = "http://api.worldbank.org/v2/country?format=json&per_page=300"
    response = requests.get(countries_url)

    if response.status_code == 200:
        data = json.loads(response.text)
        country_list = [country["id"] for country in data[1] if not country["region"]["value"].startswith("Aggregates")]
    else:
        print(f"Ошибка запроса списка стран: {response.status_code}")
    return country_list
indicator_code = 'NY.GDP.MKTP.KD'

def get_all_countries(country_list, indicator_code):
    country_gdp_data = {}

# Получаем данные ВВП для каждой страны
    for country_code in country_list:
        url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&per_page=60"
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)
            if data[1] is None:
                continue
            # Извлекаем данные и создаем словарь
            for entry in data[1]:
                country_name = entry['country']['value']
                year = entry['date']
                gdp = entry['value']

                if country_name not in country_gdp_data:
                    country_gdp_data[country_name] = {}

                country_gdp_data[country_name][year] = gdp

        else:
            print(f"Ошибка запроса данных ВВП для страны {country_code}: {response.status_code}")
    return country_gdp_data


# Преобразуем словарь в датафрейм


