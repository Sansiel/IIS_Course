# Sex & Country dependence Suicide by Sansiel(nickname)

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from itertools import groupby
import seaborn as sb
from numpy import mean

data = pd.read_csv('D:/mega/УлГТУ/4.1 курс/ИИС (Власенко)/Курсач/master.csv')

dataCountry = []
for i in data.country:
    dataCountry.append(i)
dataCountry = [el for el, _ in groupby(dataCountry)]


# Графики по странам, я это в архиве прислал, оно долгое, лучше не запускай.

countContry=0
while countContry < len(dataCountry)-5:
    fig, axs = plt.subplots( len(dataCountry[countContry:countContry+5]))
    count=0
    l = dataCountry[countContry:countContry+5]
    fig.suptitle(str(l))
    for i in dataCountry[countContry:countContry+5]:
        sgsc = data.loc[(data.country==i), :]
        axs[count].plot('year','suicides/100k pop', data=sgsc.loc[sgsc.sex=="male",:],c="blue")
        axs[count].plot('year','suicides/100k pop', data=sgsc.loc[sgsc.sex=="female",:],c="red")
        axs[count].legend(("Male","Female"))
        count+=1
    plt.savefig("plots"+str(countContry)+".png")
    countContry+=5

    # plt.clf() #Это не нужно для работы



data=data.rename(columns={'country':'Country',
                          'year':'Year',
                          'sex':'Sex',
                          'age':'Age',
                          'suicides_no':'SuicidesNo',
                          'population':'Population',
                          'suicides/100k pop':'Suicides100kPop',
                          'country-year':'CountryYear',
                          'HDI for year':'HDIForYear',
                          ' gdp_for_year ($) ':'GdpForYear',
                          'gdp_per_capita ($)':'GdpPerCapita',
                          'generation':'Generation'})

plt.clf()
# Топ 10 стран по кол-ву суицидов
df = data.groupby(['Country'])
df.Suicides100kPop.mean().nlargest(10).plot(kind='barh')
plt.xlabel("Avg. Number of Suicides per 100k (1985-2015)")
plt.title("Top 10 Countries by Prop. of Suicides per 100k")
# plt.show()
plt.savefig("Top 10 Countries by Prop. of Suicides per 100k.png")

plt.clf()
# Зависимость от пола
df = data.groupby(['Sex'])
df.Suicides100kPop.sum().plot(kind='pie', autopct='%1.1f%%', label='World Suicides by Sex')
# plt.show()
plt.savefig("World Suicides by Sex.png")


# Age
sb.catplot(x='Sex', y='SuicidesNo', col='Age', data=data, estimator=mean, kind='bar', col_wrap=3, ci=False, col_order=['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years'])
plt.savefig("Age statiscis.png")

