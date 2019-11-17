import pandas as pd

df = pd.read_csv('./WebVisualizations/Resources/cities.csv')

output = df.to_html()

print(output)