# Используя код из пункта «Решение задачи ранжирования признаков», выполните ранжирование признаков с 
# помощью указанных по варианту. Отобразите получившиеся значения\оценки каждого признака каждым 
# методом\моделью и среднюю оценку. Проведите анализ получившихся результатов. 
# Какие 4 признака оказались самыми важными по среднему значению? (Названия\индексы признаков и 
# будут ответом на задание). 
# Вариант 3 (23). 
#   Линейная регрессия (LinearRegression) , 
#   Сокращение признаков Случайными деревьями (Random Forest Regressor), 
#   Линейная корреляция (f_regression)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import numpy as np 
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import f_regression
#генерируем исходные данные: 750 строк-наблюдений и 14 столбцов-признаков
np.random.seed(0)
size = 750
X = np.random.uniform(0, 1, (size, 14))
#Задаем функцию-выход: регрессионную проблему Фридмана
Y = (10 * np.sin(np.pi*X[:,0]*X[:,1]) + 20*(X[:,2] - .5)**2 + 10*X[:,3] + 5*X[:,4]**5 + np.random.normal(0,1))
#Добавляем зависимость признаков
X[:,10:] = X[:,:4] + np.random.normal(0, .025, (size,4))

#LinearRegression
lr = LinearRegression()
lr.fit(X, Y)
#Random Forest Regressor
rfr = RandomForestRegressor()
rfr.fit(X, Y)
rf=rfr.predict(X)[0:14]
#f_regression
fr = f_regression(X, Y)
fr = fr[0]

names = ["x%s" % i for i in range(1,15)]

def rank_to_dict(ranks, names):
    ranks = np.abs(ranks)
    minmax = MinMaxScaler()
    ranks = minmax.fit_transform(np.array(ranks).reshape(14,1)).ravel()
    ranks = map(lambda x: round(x, 2), ranks)
    return dict(zip(names, ranks))

ranks={}
ranks["Linear Regression"] = rank_to_dict(lr.coef_, names)
ranks["Random Forest Regressor"] = rank_to_dict(rf, names)
ranks["f_regression"] = rank_to_dict(fr, names)

#Создаем пустой список для данных
mean = {}
#«Бежим» по списку ranks
for key, value in ranks.items():
#«Пробегаемся» по списку значений ranks, которые являются парой имя:оценка
    for item in value:
#имя будет ключом для нашего mean
#если элемента с текущим ключем в mean нет - добавляем
        if(item not in mean):
            mean[item] = 0
#суммируем значения по каждому ключу-имени признака
        mean[item] += value[item]
#находим среднее по каждому признаку
for value in mean:
    res=mean[value]/len(ranks)
    mean[value] = round(res, 2)
#сортируем и распечатываем список
mean = {k: v for k, v in sorted(mean.items(), key=lambda item: item[1])}
print ("MEAN")
print (mean)

for key in ranks:
    ranks[key] = {k: v for k, v in sorted(ranks[key].items(), key=lambda item: item[1])}
for key in ranks:
    print (key)
    print (ranks[key])