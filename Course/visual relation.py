import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid") 
import seaborn as sns
# from wordcloud import WordCloud


suicideDataRaw = pd.read_csv('D:/mega/УлГТУ/4.1 курс/ИИС (Власенко)/Курсач/master.csv')
suicideData = suicideDataRaw.copy()

suicideData.rename(columns={'suicides_no':'suicides_number',
                            'suicides/100k pop':'suicides_per_100k_pop',
                            ' gdp_for_year ($) ':'gdp_for_year', 
                       'gdp_per_capita ($)':'gdp_per_capital'}, inplace=True)
suicideData.columns = suicideData.columns.str.replace(" ","_")
suicideData.columns = suicideData.columns.str.lower()
#Remove country-year feature
suicideData.drop("country-year", axis = 1, inplace = True)
#Remove feature
suicideData.drop("hdi_for_year", axis = 1, inplace = True)

# Correlation Between Year -- Suicide Numbers -- Population -- Suicides per 100k Population -- GDP for year -- GDP per capital
numericVars = ["year","suicides_number", "population", "suicides_per_100k_pop", 
         "gdp_for_year", "gdp_per_capital"]
sns.heatmap(suicideData[numericVars].corr(), annot = True, fmt = ".2f")
plt.savefig("Correlation Between Year -- Suicide Numbers -- Population -- Suicides per 100k Population -- GDP for year -- GDP per capital")


#Suicide Numbers vs Population by Generation and Gender
plt.figure(figsize=(12,8))
ax = sns.scatterplot(x="suicides_number", 
                     y="population",
                     hue="generation", 
                     style="sex", 
                     data=suicideData)
plt.xlabel('Suicide Number')
plt.ylabel('Population')
plt.title('Suicide Numbers vs Population by Generation and Gender')
plt.savefig("Suicide Numbers vs Population by Generation and Gender")


#Suicide Numbers vs GDP for Year by Generation and Gender
plt.figure(figsize=(12,8))
ax = sns.scatterplot(x="suicides_number", 
                     y="gdp_for_year",
                     hue="generation", 
                     style="sex", 
                     data=suicideData)
plt.xlabel('Suicide Number')
plt.ylabel('GDP for Year')
plt.title('Suicide Numbers vs GDP for Year by Generation and Gender')
plt.savefig('Suicide Numbers vs GDP for Year by Generation and Gender')


#GDP for Capital vs GDP for Year by Generation and Gender
plt.figure(figsize=(12,8))
ax = sns.scatterplot(x="gdp_per_capital", 
                     y="gdp_for_year",
                     hue="generation", 
                     style="sex", 
                     data=suicideData)
plt.xlabel('GDP per Capital')
plt.ylabel('GDP for Year')
plt.title('GDP for Capital vs GDP for Year by Generation and Gender')
plt.savefig('GDP for Capital vs GDP for Year by Generation and Gender')


#GDP for Year vs Population by Generation and Gender
plt.figure(figsize=(12,8))
ax = sns.scatterplot(x="gdp_for_year", 
                     y="population",
                     hue="generation", 
                     style="sex", data=suicideData)
plt.xlabel('GDP for Year')
plt.ylabel('Population')
plt.title('GDP for Year vs Population by Generation and Gender')
plt.savefig('GDP for Year vs Population by Generation and Gender')