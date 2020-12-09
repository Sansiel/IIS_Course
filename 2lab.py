# По данным о пассажирах Титаника решите задачу классификации (с помощью дерева решений), 
# в которой по различным характеристикам пассажиров требуется найти у выживших пассажиров
# два наиболее важных признака из трех рассматриваемых (по варианту - Sex,Age,SibSp).
import numpy as np #Нигде не применён, но вообще удобная библиотека для работы с матрицами.
import pandas as pd #Применён для работы с таблицей csv. 
# Используется для манипулирования числовым таблицами и временными рядами Также строится поверх NumPy.
from sklearn.tree import DecisionTreeClassifier #Библиотека sklearn используется для машинного обучения. 
#В данном случае подгружается модуль для работы с деревьями решений

#Считываем таблицу
data = pd.read_csv('D:/mega/УлГТУ/4.1 курс/ИИС (Власенко)/titanic.csv', index_col='PassengerId')
#Формируем фрэйм с нужными столбцами
main_data_frame = pd.DataFrame(data=data, columns=['Age', 'Sex', 'SibSp', 'Survived'])
#очищаем от пустот
main_data_frame = main_data_frame[["Age", "Sex", "SibSp", "Survived"]].dropna()  
# Заменяем необрабатываемые значения на обрабатываемые. 
output = main_data_frame[["Age", "Sex", "SibSp"]].replace("female",0).replace("male",1)
# Задаём объект вызова модуля
clf = DecisionTreeClassifier()
# Выделяем определяющие значения
Y = main_data_frame['Survived']
# Меняем название переменной, просто так, чтобы было типо как функция из х, у. Прикольно же?
X = output
# Вызываем функцию и передам аргументы.
clf.fit(X, Y)
# Принтим в консоль
print(clf.feature_importances_)
print(sum(clf.feature_importances_)) #Это была проверка на то, что сумма = 1.