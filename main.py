import pandas as pd
import plotly.express as px

# Вместо 'selected_df', я использую 'df' для примера
# Создайте свой DataFrame 'selected_df' со столбцом 'Date' в качестве индекса
data = {'Country1': [1230, 2340, 3450],
        'Country2': [3210, 6540, 9870]}
index = pd.date_range('2020-01-01', periods=3, freq='Y')

df = pd.DataFrame(data, index=index)

# Преобразование данных без изменения индекса
df_stacked = df.stack().reset_index()
df_stacked.columns = ['Date', 'Country', 'GDP']

# Создание интерактивного графика с помощью Plotly Express
fig = px.line(df_stacked, x='Date', y='GDP', color='Country', title='GDP by Country')

# Отображение графика
fig.show()