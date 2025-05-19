# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:05:55 2023

@author: flavio
"""

# Tratamiento de datos
# ==============================================================================
import pandas as pd
import numpy as np

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from mlxtend.plotting import plot_decision_regions

# Preprocesado y modelado
# ==============================================================================
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Configuración matplotlib
# ==============================================================================
plt.rcParams['image.cmap'] = "bwr"
#plt.rcParams['figure.dpi'] = "100"
plt.rcParams['savefig.bbox'] = "tight"
style.use('ggplot') or plt.style.use('ggplot')

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

dataFruit = pd.read_csv("FruitBD.csv")
xFruit = dataFruit.iloc[:, [2,8,15,23]].values
yFruit = dataFruit['Clase']

xFruit = StandardScaler().fit_transform(xFruit)
xFruitTrain, xFruitTest, yFruitTrain, yFruitReal = train_test_split(xFruit, yFruit, test_size=0.2)

""" Naive Bayes - Classification """

modelNB = GaussianNB()
modelNB.fit(xFruitTrain, yFruitTrain)

yFruitPred = modelNB.predict(xFruitTest)

cm = metrics.confusion_matrix(yFruitReal, yFruitPred)
metrics.ConfusionMatrixDisplay(confusion_matrix=cm).plot()

metrics.precision_score(yFruitReal, yFruitPred, average='macro')
metrics.recall_score(yFruitReal, yFruitPred, average='macro')
metrics.accuracy_score(yFruitReal, yFruitPred)

""" Naive Bayes - All features """

xFruit = dataFruit.drop('Clase', axis=1)
xFruit = StandardScaler().fit_transform(xFruit)
xFruitTrain, xFruitTest, yFruitTrain, yFruitReal = train_test_split(xFruit, yFruit, test_size=0.2)

modelNB = GaussianNB()
modelNB.fit(xFruitTrain, yFruitTrain)

yFruitPred = modelNB.predict(xFruitTest)

cm = metrics.confusion_matrix(yFruitReal, yFruitPred)
metrics.ConfusionMatrixDisplay(confusion_matrix=cm).plot()

metrics.precision_score(yFruitReal, yFruitPred, average='macro')
metrics.recall_score(yFruitReal, yFruitPred, average='macro')
metrics.accuracy_score(yFruitReal, yFruitPred)

""" k-NN - Classification """

modelkNN = KNeighborsClassifier(n_neighbors=3, metric='minkowski', p=2)  
modelkNN.fit(xFruitTrain, yFruitTrain)

yFruitPred = modelkNN.predict(xFruitTest)

cm = metrics.confusion_matrix(yFruitReal, yFruitPred)
metrics.ConfusionMatrixDisplay(confusion_matrix=cm).plot()

metrics.precision_score(yFruitReal, yFruitPred, average='macro')
metrics.recall_score(yFruitReal, yFruitPred, average='macro')
metrics.accuracy_score(yFruitReal, yFruitPred)

""" k-NN - Classification """

params = {
    'n_neighbors':  range(1, 15, 2),
    'p': [1,2],
    'weights': ['uniform', 'distance']
}

clf = GridSearchCV( estimator=KNeighborsClassifier(), param_grid=params, cv=5, n_jobs=5,verbose=1)

clf.fit(xFruitTrain, yFruitTrain)
print(clf.best_params_)

modelkNN = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=1, weights='distance')  
modelkNN.fit(xFruitTrain, yFruitTrain)

yFruitPred = modelkNN.predict(xFruitTest)

cm = metrics.confusion_matrix(yFruitReal, yFruitPred)
metrics.ConfusionMatrixDisplay(confusion_matrix=cm).plot()

metrics.precision_score(yFruitReal, yFruitPred, average='macro')
metrics.recall_score(yFruitReal, yFruitPred, average='macro')
metrics.accuracy_score(yFruitReal, yFruitPred)

""" SVM - Classification """

# Datos
# ==============================================================================
url = 'https://raw.githubusercontent.com/JoaquinAmatRodrigo/' \
       + 'Estadistica-machine-learning-python/master/data/ESL.mixture.csv'
datos = pd.read_csv(url)
datos.head(3)

fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(datos.X1, datos.X2, c=datos.y);
ax.set_title("Datos ESL.mixture");

# División de los datos en train y test
# ==============================================================================
X = datos.drop(columns = 'y')
y = datos['y']

X_train, X_test, y_train, y_test = train_test_split(X, y.values.reshape(-1,1),
                         train_size = 0.8, random_state = 1234, shuffle = True)

# Creación del modelo SVM lineal
# ==============================================================================
modelo = SVC(C = 100, kernel = 'linear', random_state=123)
modelo.fit(X_train, y_train)

# Representación gráfica de los límites de clasificación
# ==============================================================================
# Grid de valores
x = np.linspace(np.min(X_train.X1), np.max(X_train.X1), 50)
y = np.linspace(np.min(X_train.X2), np.max(X_train.X2), 50)
Y, X = np.meshgrid(y, x)
grid = np.vstack([X.ravel(), Y.ravel()]).T

# Predicción valores grid
pred_grid = modelo.predict(grid)

fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(grid[:,0], grid[:,1], c=pred_grid, alpha = 0.2)
ax.scatter(X_train.X1, X_train.X2, c=y_train, alpha = 1)

# Vectores soporte
ax.scatter(
    modelo.support_vectors_[:, 0],
    modelo.support_vectors_[:, 1],
    s=200, linewidth=1,
    facecolors='none', edgecolors='black'
)

# Hiperplano de separación
ax.contour(X, Y, modelo.decision_function(grid).reshape(X.shape),
    colors = 'k',
    levels = [-1, 0, 1],
    alpha  = 0.5,
    linestyles = ['--', '-', '--']
)

# Predicciones test
# ==============================================================================
predicciones = modelo.predict(X_test)
predicciones

# Accuracy de test del modelo 
# ==============================================================================
accuracy = accuracy_score(
            y_true    = y_test,
            y_pred    = predicciones,
            normalize = True
           )
print("")
print(f"El accuracy de test es: {100*accuracy}%")


# SVM radial
# Grid de hiperparámetros
# ==============================================================================
param_grid = {'C': np.logspace(-5, 7, 20)}

# Búsqueda por validación cruzada
# ==============================================================================
grid = GridSearchCV(
        estimator  = SVC(kernel= "rbf", gamma='scale'),
        param_grid = param_grid,
        scoring    = 'accuracy',
        n_jobs     = -1,
        cv         = 3, 
        verbose    = 0,
        return_train_score = True
      )

# Se asigna el resultado a _ para que no se imprima por pantalla
_ = grid.fit(X = X_train, y = y_train)

# Resultados del grid
# ==============================================================================
resultados = pd.DataFrame(grid.cv_results_)
resultados.filter(regex = '(param.*|mean_t|std_t)')\
    .drop(columns = 'params')\
    .sort_values('mean_test_score', ascending = False) \
    .head(5)

# Mejores hiperparámetros por validación cruzada
# ==============================================================================
print("----------------------------------------")
print("Mejores hiperparámetros encontrados (cv)")
print("----------------------------------------")
print(grid.best_params_, ":", grid.best_score_, grid.scoring)

modelo = grid.best_estimator_

# Representación gráfica de los límites de clasificación
# ==============================================================================
# Grid de valores
x = np.linspace(np.min(X_train.X1), np.max(X_train.X1), 50)
y = np.linspace(np.min(X_train.X2), np.max(X_train.X2), 50)
Y, X = np.meshgrid(y, x)
grid = np.vstack([X.ravel(), Y.ravel()]).T

# Predicción valores grid
pred_grid = modelo.predict(grid)

fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(grid[:,0], grid[:,1], c=pred_grid, alpha = 0.2)
ax.scatter(X_train.X1, X_train.X2, c=y_train, alpha = 1)

# Vectores soporte
ax.scatter(
    modelo.support_vectors_[:, 0],
    modelo.support_vectors_[:, 1],
    s=200, linewidth=1,
    facecolors='none', edgecolors='black'
)

# Hiperplano de separación
ax.contour(
    X,
    Y,
    modelo.decision_function(grid).reshape(X.shape),
    colors='k',
    levels=[0],
    alpha=0.5,
    linestyles='-'
)

ax.set_title("Resultados clasificación SVM radial");

# Representación gráfica utilizando plot_decision_regions() de mlxtend
# ==============================================================================
fig, ax = plt.subplots(figsize=(6,4))
plot_decision_regions(
    X = X_train.to_numpy(),
    y = y_train.flatten(),
    clf = modelo,
    ax = ax
)
ax.set_title("Resultados clasificación SVM radial");

# Predicciones test
# ==============================================================================
predicciones = modelo.predict(X_test)

# Accuracy de test del modelo 
# ==============================================================================
accuracy = accuracy_score(
            y_true    = y_test,
            y_pred    = predicciones,
            normalize = True
           )
print("")
print(f"El accuracy de test es: {100*accuracy}%")

# Matriz de confusión de las predicciones de test
# ==============================================================================
confusion_matrix = pd.crosstab(
    y_test.ravel(),
    predicciones,
    rownames=['Real'],
    colnames=['Predicción']
)
confusion_matrix