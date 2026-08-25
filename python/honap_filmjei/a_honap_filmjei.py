import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import requests
from io import StringIO

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

year = 2026
month = ""
while not month.isdecimal():
    month = input("Chose a month (january = 1, february = 2, etc.): ")
month = int(month)
months = ['January','February','March','April','May','June','July','August','September','October','November','December']


headers = {
    'User-Agent': 'Mozilla/5.0'
}
response = requests.get(f'https://web.archive.org/web/20251204002345/https://www.the-numbers.com/movies/upcoming/2026', headers = headers)
response.raise_for_status()
tables = pd.read_html(StringIO(response.text))

df = tables[1][['Release Date','Movie']].dropna(how = 'all').reset_index(drop = True)
df['Release Date'] = df['Release Date'].ffill()
next_month_df = df[df['Release Date'].str.contains(months[month - 1])]

title  = f'########## Movie releases of {year} {months[month - 1]} ##########'
border = '#' * len(title)

print()
print(border)
print(border)
print(title)
print(border)
print(border)
print()

print(next_month_df)
next_month_df.to_excel("output.xlsx")