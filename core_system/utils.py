import pandas as pd


export_const_dol = pd.read_csv('data/EGS_const_dol.csv')
export_const_dol = export_const_dol.set_index('Unnamed: 0')

import_const_dol = pd.read_csv('data/IGS_сonst_dol.csv')
import_const_dol = import_const_dol.set_index('Unnamed: 0')

export_cur_dol = pd.read_csv('data/EGS_cur_dol.csv')
export_cur_dol = export_cur_dol.set_index('Unnamed: 0')

import_cur_dol = pd.read_csv('data/IGS_cur_dol.csv')
import_cur_dol = import_cur_dol.set_index('Unnamed: 0')

export_const_lcu = pd.read_csv('data/EGS_const_lcu.csv')
export_const_lcu = export_const_lcu.set_index('Unnamed: 0')

import_const_lcu = pd.read_csv('data/IGS_const_lcu.csv')
import_const_lcu = import_const_lcu.set_index('Unnamed: 0')

export_cur_lcu = pd.read_csv('data/EGS_cur_lcu.csv')
export_cur_lcu = export_cur_lcu.set_index('Unnamed: 0')

import_cur_lcu = pd.read_csv('data/IGS_cur_lcu.csv')
import_cur_lcu = import_cur_lcu.set_index('Unnamed: 0')

gdp = pd.read_csv('data/GDP.csv')
gdp = gdp.set_index('Unnamed: 0')


def diff_dataframes(df1, df2):
    # Найти общие столбцы
    common_columns = list(set(df1.columns[1:]) & set(df2.columns[1:]))

    # Вычислить разницу между значениями одинаковых столбцов
    diff_df = df1[common_columns].subtract(df2[common_columns])

    return diff_df


net_export_const_dol = diff_dataframes(export_const_dol, import_const_dol)
net_export_cur_dol = diff_dataframes(export_cur_dol, import_cur_dol)
net_export_const_lcu = diff_dataframes(export_const_lcu, import_const_lcu)
net_export_cur_lcu = diff_dataframes(export_cur_lcu, import_cur_lcu)
if __name__ == '__main__':
    print(net_export_const_dol(export_const_dol, import_const_dol))

