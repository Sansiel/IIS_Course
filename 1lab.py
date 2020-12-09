# Какую долю пассажиры первого класса составляли среди всех пассажиров? 
# Ответ приведите в процентах (число в интервале [0;100], знак процента не нужен), округлив до двух знаков.
import pandas
data = pandas.read_csv('D:\\mega\\УлГТУ\\4.1 курс\\ИИС (Власенко)\\titanic.csv')

class1, summ = 0, 0

for index, row in data.iterrows(): 
    if str(row[2])== "1": class1=class1+1 
    if str(row[2])== "2": summ=summ+1
    if str(row[2])== "3": summ=summ+1
    if str(row[2])== "4": summ=summ+1
    
summ=summ+class1
print(round(class1*(100/summ),2))  #доля первого класса