import pandas as pd
from pandas import DataFrame
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('terro_attack.csv', encoding= 'latin-1', low_memory=False)

'''Getting the target of the terrorist during a period of time and display it on a chart bar'''
'''70's Attack target'''
Target = data[data.targtype1T == 'Business']
year = Target[Target.year <= 1979]
count = year.shape
Bu70s = count[0]

Target = data[data.targtype1T == 'Police']
year = Target[Target.year <= 1979]
count = year.shape
Pl70s = count[0]

Target = data[data.targtype1T == 'Military']
year = Target[Target.year <= 1979]
count = year.shape
Ml70s = count[0]

'''80's Attack Target'''
Target = data[data.targtype1T == 'Business']
year = Target[Target.year <= 1989]
year1 = year[year.year >= 1980]
count = year1.shape
Bu80s = count[0]

Target = data[data.targtype1T == 'Police']
year = Target[Target.year <= 1989]
year1 = year[year.year >= 1980]
count = year1.shape
Pl80s = count[0]

Target = data[data.targtype1T == 'Military']
year = Target[Target.year <= 1989]
year1 = year[year.year >= 1980]
count = year1.shape
Ml80s = count[0]

'''90's Attack Target'''
Target = data[data.targtype1T == 'Business']
year = Target[Target.year <= 1999]
year1 = year[year.year >= 1990]
count = year1.shape
Bu90s = count[0]

Target = data[data.targtype1T == 'Police']
year = Target[Target.year <= 1999]
year1 = year[year.year >= 1990]
count = year1.shape
Pl90s = count[0]

Target = data[data.targtype1T == 'Military']
year = Target[Target.year <= 1999]
year1 = year[year.year >= 1990]
count = year1.shape
Ml90s = count[0]

year = ["70's", "70's", "70's", "80's", "80's", "80's", "90's", "90's", "90's"]
target = ['Business', 'Police', 'Military','Business','Police','Military','Business','Police','Military']
counter = [Bu70s, Pl70s, Ml70s, Bu80s, Pl80s,Ml80s, Bu90s, Pl90s, Ml90s]

FrData = DataFrame({'Year': year, 'Target': target, 'Counter': counter})

print(FrData)

sns.barplot(x = FrData.Year, y = FrData.Counter, hue = FrData.Target, data = FrData, palette = "Set1")

sns.plt.show()
