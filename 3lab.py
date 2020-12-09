# Используя код из пункта «Регуляризация и сеть прямого распространения», сгенерируйте определенный
# тип данных и сравните на нем 3 модели (по варианту).  Постройте графики, отобразите качество моделей, 
# объясните полученные результаты. 
# Вариант 2 (23).	
# Данные: make_circles (noise=0.2, factor=0.5, random_state=rs)
# Модели:
#     Линейную регрессию 
#     Полиномиальную регрессию (со степенью 3) 
#     Гребневую полиномиальную регрессию (со степенью 3, alpha = 1.0) 
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from matplotlib.pyplot import clf

circles_dataset = make_circles (noise=0.2, factor=0.5, random_state=1)

X, y = circles_dataset
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4, random_state=42)
alphas = np.logspace(-5, 1, 5)
current_subplot= plt.subplot(1, 5 + 1, 1)

cm = plt.cm.RdBu
cm_bright = ListedColormap(['#FF0000', '#0000FF'])
current_subplot.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright)
current_subplot.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,alpha=0.6)

# plt.show()
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
 
model = LinearRegression().fit(X,y)
print('Linear coefficient of determination:', model.score(X,y))
y_=model.predict(X)
plt.plot(X, y_, color='blue', linewidth=1)

model = Pipeline([('poly', PolynomialFeatures(degree=3)), ('linear', LinearRegression())])
model = model.fit(X, y)
print('Polynomial coefficient of determination:', model.score(X,y))
y_=model.predict(X)
plt.plot(X, y_, color='Red', linewidth=1)
# true_fun = lambda X: np.cos(1.5 * np.pi * X)
# plt.plot(X, model.predict(X), label="Model")
# plt.plot(X, true_fun(X), label="True function")

model = Pipeline([('poly', PolynomialFeatures(degree=3)), ('ridge', Ridge(alpha=1.0))])
model = model.fit(X, y)
print('Ridge coefficient of determination:', model.score(X,y))
y_=model.predict(X)
plt.plot(X, y_, color='Purple', linewidth=1)

# plt.axis([-1,1,-0.5,0.5])
plt.show()




#Градиент
# h = .02 #шаг регулярной сетки
# x0_min, x0_max = X[:, 0].min() - .5, X[:, 0].max() + .5
# x1_min, x1_max = X[:, 1].min() - .5, X[:, 1].max() + .5
# xx0, xx1 = np.meshgrid(np.arange(x0_min, x0_max, h), np.arange(x1_min, x1_max, h))
# Z = clf.decision_function(np.c_[xx0.ravel(), xx1.ravel()])#1
# Z = clf.predict_proba(np.c_[xx0.ravel(), xx1.ravel()])[:, 1]#2
# Z = clf.predict(np.c_[xx0.ravel(),xx1.ravel()])#3
# hasattr(clf, "decision_function")
# Z = Z.reshape(xx0.shape)
# current_subplot.contourf(xx0, xx1, Z, cmap=cm, alpha=.8)
# current_subplot.set_xlim(xx0.min(),xx0.max())
# current_subplot.set_ylim(xx0.min(),xx1.max())
# current_subplot.set_xticks(())
# current_subplot.set_yticks(())
# # current_subplot.set_title(name)
# # current_subplot.text(xx0.max() - .3, xx1.min() + .3, ('%.2f' % score).lstrip('0'), size=15, horizontalalignment='right')
# current_subplot.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,alpha=0.6)
# plt.show()