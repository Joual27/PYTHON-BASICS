import pandas as pd
import numpy as np


TARGET_URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

tables = pd.read_html(TARGET_URL)

df = tables[3]
df.columns = range(df.shape[1])
df = df[[0, 2]]
df = df.iloc[1:11, :]

df.columns = ['Country', 'GDP (MILLION USD)']

df[['GDP (MILLION USD)']] = df[['GDP (MILLION USD)']].astype(int)
df[['GDP (MILLION USD)']] = df[['GDP (MILLION USD)']]/1000
df[['GDP (MILLION USD)']] = np.round(df[['GDP (MILLION USD)']],2)
df.rename(columns={ 'GDP (MILLION USD)' : 'GDP (BILLION USD)'}, inplace=True)

print(df)
#
# df.to_csv('Largest_economies.csv')


