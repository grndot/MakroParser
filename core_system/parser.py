import requests
import json
import pandas as pd


indicator_codes = {'IGS_const_dol': 'NE.IMP.GNFS.KD', 'IGS_cur_lcu': 'NE.IMP.GNFS.CN',
                   'IGS_cur_dol': 'NE.IMP.GNFS.CD', 'IGS_const_lcu': 'NE.IMP.GNFS.KN',
                   'EGS_const_lsu': 'NE.EXP.GNFS.KN', 'EGS_cur_dol': 'NE.EXP.GNFS.CD',
                   'EGS_cur_lsu': 'NE.EXP.GNFS.CN', 'EGS_const_dol': 'NE.EXP.GNFS.KD'}
# Получаем список всех стран
def get_all_country_names():
    countries_url = "http://api.worldbank.org/v2/country?format=json&per_page=300"
    response = requests.get(countries_url)

    if response.status_code == 200:
        data = json.loads(response.text)
        country_list = [country["id"] for country in data[1] if not country["region"]["value"].startswith("Aggregates")]
    else:
        country_list = []
        print(f"Ошибка запроса списка стран: {response.status_code}")
    return country_list



def get_all_countries(country_list, indicator_code):
    country_data = {}

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

                if country_name not in country_data:
                    country_data[country_name] = {}

                country_data[country_name][year] = gdp

        else:
            print(f"Ошибка запроса данных ВВП для страны {country_code}: {response.status_code}")
    return pd.DataFrame(country_data)


if __name__ == '__main__':
    indicator_code = 'NE.EXP.GNFS.KD'
    country_names = get_all_country_names()
    df = get_all_countries(country_names, indicator_code)
    print(df)
    df.to_csv('../data/EGS_const_dol.csv')


