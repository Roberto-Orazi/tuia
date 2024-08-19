## Inteligencia artificial?
Es que una maquina que pueda pensar o actuar como un humano

## Aprendizaje automatico(Machine Learning)
Es el aprendizaje de maquina, se usa para aprender y mejorar a partir de datos.

### Enfoque tradicional
Datos + reglas = resultado Nosotros tenemos datos y reglas para llegar a un resultado

### Enfoque ML
Datos + resultados = reglas Nosotros tenemos datos y los resultados para decifrar las reglas

## Pasos para resolver un problema

1. Estudiar el problema
2. Entrenar el modelo de ml(con mucha data)
3. Tenemos la solucion
4. Inspeccionamos la solucion
5. Con la solucion tenemos mejor entendimiento de un problema
6. Y repetimos si es necesario


## Aprendizajes
### Supervisado
El algoritmo recibe un conjunto de datos de entrenamiento con ejemplos etiquetados. El objetivo es aprender una funcion
que pueda mapear las entradas(caracteristicas) a las salidas(etiquetas) correspondientes

### No supervidado
A diferencia del otro no tengo etiquetas. El objetivo es descubrir patrones y estructuras ocultas en los datos sin guia
explicita. Uso: Problemas de agrupamiento y reduccion de dimensionalidad.

### Por refuerzo
La maquina toma decisiones en funcion del estado actual y recibe recompensas o castigos del entorno en funcion de las
decisiones. El objetivo es aprender una politica que maximice la recompensa a largo plazo


## Clasificacion VS Regresion
### Tipos de aprendizaje supervisado
#### Clasificacion
La clasficacion precide una etiqueta o clase a partir de un conjunto de claracteristicas.

- Deteccion de spam (email)
- Reconocimiento facial
- Deteccion de fraude
- Identificacion de señales de transito
- Prediccion de dia lluvioso Hay problemas de dos clases o multiclase

#### Regresion
La regresion se utiliza para predecir un valor numerico continuo.

- Prediccion de precios de un determinado producto
- Prediccion de valores futuros de instrumentos financieros
- Prediccion de consumo de energia electrica
- Prediccion de cantidad de lluvia

## Pipeline de datos
1. Conjunto de datos
2. Particion en conjuntos de entrenamiento, validacion y prueba
3. Preprocesamiento de valores faltantes
4. Computdo de media, desvio y cuantiles
5. Estandarizacion de datos
6. Ingenieria de caracteristicas



## Exploratory data analysis
- Distribucion de data
- Datos faltantes
- Outliers: Son los valores que se alejan significativamente del resto de los datos.
- Correlacion
- patrones
- tipos de datos: categoricos o numericos
- visualizacion de datos
- calidad de los datos

## Pipeline de tareas sobre el conjunto de entrenamiento
1. Conjunto de entrenamiento
2. Definir metricas de evaluacion
3. Calculo de metricas para el modelo base
4. Entrenar un modelo
5. Computar metricas de validacion
6. optimizacion de hiperpametros -> punto 4
7. Evaluar metricas en el conjunto de prueba


## Algoritmos ML
### Funcion de perdida
- Funcion para minimizar, a menor valor, mejora la performance
- Se elige la funcion del problema:
 - Regresion MSE
 - Clasificacion BCE

### Optimizador
- Algoritmo que efectua la optimizacion de la funcion de perdida
- ejemplo: Gradiente desenciente(Iteraciones)