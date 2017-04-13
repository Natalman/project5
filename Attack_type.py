import pandas as pd
from pandas import DataFrame
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('terro_attack.csv', encoding= 'latin-1', low_memory=False)


'''70's attack data'''
AttackType = data[data.attacktypeT == 'Assassination']
year = AttackType[AttackType.year <= 1979]
count = year.shape
Assas70s = count[0]

AttackType = data[data.attacktypeT == 'Bombing/Explosion']
year = AttackType[AttackType.year <= 1979]
count = year.shape
Bomb70s = count[0]

'''80's attack data'''
AttackType = data[data.attacktypeT == 'Assassination']
year = AttackType[AttackType.year <= 1989]
year1 = year[year.year >= 1980]
count = year1.shape
Assas80s = count[0]

AttackType = data[data.attacktypeT == 'Bombing/Explosion']
year = AttackType[AttackType.year <= 1989]
year1 = year[year.year >= 1980]
count = year1.shape
Bomb80s = count[0]

'''90's attack data'''
AttackType = data[data.attacktypeT == 'Assassination']
year = AttackType[AttackType.year <= 1999]
year1 = year[year.year >= 1990]
count = year1.shape
Assas90s = count[0]

AttackType = data[data.attacktypeT == 'Bombing/Explosion']
year = AttackType[AttackType.year <= 1999]
year1 = year[year.year >= 1990]
count = year1.shape
Bomb90s = count[0]

year = ["70's", "70's", "80's", "80's", "90's", "90's"]
AttackType = ['Assasination', 'Bombing/Explosion', 'Assasination', 'Bombing/Explosion', 'Assasination', 'Bombing/Explosion']
counter = [Assas70s, Bomb70s, Assas80s, Bomb80s, Assas90s, Bomb90s]



FrData = DataFrame({'Year': year, 'AttackType': AttackType, 'Count': counter})

print(FrData)

# sns.boxplot(x = 'Year', y = 'Count', hue = 'AttackType', data = FrData, palette = "PRGn" )
# nn = sns.despine(offset = 10, trim = True)

sns.barplot(x = FrData.Year, y = FrData.Count, hue = FrData.AttackType, data = FrData, palette = "PRGn")

sns.plt.show()
