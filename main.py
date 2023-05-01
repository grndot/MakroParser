import plotly.graph_objects as go
import plotly.io as pio

x = [1, 2, 3, 4]
y = [10, 15, 13, 17]

trace = go.Scatter(x=x, y=y, mode='markers+lines')

fig = go.Figure(trace)

# Сохранение графика в виде HTML-файла
pio.write_html(fig, file="example_plot.html", auto_open=True)
