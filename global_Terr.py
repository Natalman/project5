import pandas as pd
from pandas import DataFrame
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('terro_attack.csv', encoding= 'latin-1', low_memory=False)
'''Getting the countries attacked by the terrorist during a period of time and display it on a chart bar'''
'''70's data'''
country = data[data.country == 'United States']
year = country[country.year <= 1979]
count = year.shape
Us70s = count[0]

country = data[data.country == 'Japan']
year = country[country.year <= 1979]
count = year.shape
Jp70s = count[0]

country = data[data.country == 'United Kingdom']
year = country[country.year <= 1979]
count = year.shape
Uk70s = count[0]

'''80's data'''
country = data[data.country == 'United States']
year = country[country.year <= 1989]
year1 = year[year.year >= 1980]
count = year1.shape
Us80s = count[0]

country = data[data.country == 'Japan']
year = country[country.year <= 1989]
year1 = year[year.year >= 1980]
count = year1.shape
Jp80s = count[0]

country = data[data.country == 'United Kingdom']
year = country[country.year <= 1989]
year1 = year[year.year >= 1980]
count = year1.shape
Uk80s = count[0]

'''90's data'''
country = data[data.country == 'United States']
year = country[country.year <= 1999]
year1 = year[year.year >= 1990]
count = year1.shape
Us90s = count[0]

country = data[data.country == 'Japan']
year = country[country.year <= 1999]
year1 = year[year.year >= 1990]
count = year1.shape
Jp90s = count[0]

country = data[data.country == 'United Kingdom']
year = country[country.year <= 1999]
year1 = year[year.year >= 1990]
count = year1.shape
Uk90s = count[0]

year = ["70's", "70's", "70's", "80's", "80's", "80's", "90's", "90's", "90's"]
country = ['United States', 'Japan', 'United Kingdom','United States', 'Japan', 'United Kingdom','United States', 'Japan', 'United Kingdom']
attack = [Us70s, Jp70s, Uk70s,Us80s, Jp80s, Uk80s,Us90s, Jp90s, Uk90s]

FrData = DataFrame({'Year': year, 'Country': country, 'Attack': attack})

print(FrData)

sns.barplot(x = FrData.Year, y = FrData.Attack, hue = FrData.Country, data = FrData, palette = "muted")

sns.plt.show()
