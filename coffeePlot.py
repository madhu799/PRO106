import pandas as pd
import plotly.express as px

data = pd.read_csv("coffee.csv")
plot = px.scatter(data, x = 'Coffee in ml', y = 'sleep in hours')
plot.show()
