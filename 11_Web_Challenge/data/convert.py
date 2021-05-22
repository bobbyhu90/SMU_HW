import pandas as pd
df = pd.read_csv('weather_data.csv')
df.to_html('weather_data.html')