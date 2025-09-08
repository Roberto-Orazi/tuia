# Minería de Datos - Resumen de Unidades

## Unidad 1: Conceptos Fundamentales

## 1. Definición de Minería de Datos
- **Arte y ciencia del análisis inteligente de datos**
- **Herramientas para entender y modelizar conjuntos complejos de datos**
- **Proceso de descubrir patrones y obtener conocimiento de grandes datasets**

## 2. Paradigmas Principales (Aprendizaje Inductivo)

### Clasificación
- **Función**: `c : X → C`
- Asigna instancias a clases discretas predefinidas
- **Clasificación binaria**: C = {0, 1}
- Ejemplo: clasificar emails como spam/no spam

### Regresión
- **Función**: `f : X → ℝ`
- Predice valores numéricos continuos
- Ejemplo: predecir precio de casa basado en características

### Agrupamiento (Clustering)
- **Función**: `h : X → Ch`
- **Sin etiquetas predefinidas** (aprendizaje no supervisado)
- Descubre grupos basados en similitud
- Ejemplo: segmentación de clientes

## 3. Tipología de Algoritmos

### Supervisado
- **Clasificación**: k-NN, SVM, Redes Neuronales, Árboles de Decisión, Métodos Probabilísticos
- **Regresión**: SVM, Redes Neuronales, Árboles de Decisión, Métodos Probabilísticos

### No Supervisado
- **Clustering**: Agrupamiento Jerárquico, k-means, k-NN

### Semi-supervisado y Por Refuerzo
- Combinan datos etiquetados y no etiquetados
- Agente-ambiente con recompensas

## 4. Preparación de Datos

### Limpieza de Datos
- Detección y corrección de valores erróneos
- Gestión de valores ausentes
- Eliminación de outliers
- Resolución de inconsistencias

### Normalización de Datos
**¿Por qué?** Evitar sesgo por atributos con valores altos

**Métodos principales:**
- **Por máximo**: `zi = xi/xmax`
- **Por diferencia (Min-Max)**: `zi = (xi - xmin)/(xmax - xmin)`
- **Por desviación estándar (Z-score)**: `zi = (xi - μ)/σ`

## 5. Conjuntos de Datos

### División Estándar
- **Training**: 60-80% (entrenar modelo)
- **Validation**: 15-20% (ajustar hiperparámetros)
- **Test**: 15-20% (evaluación final)

### Validación Cruzada k-fold
- Divide datos en k particiones
- k iteraciones: cada partición es test una vez
- **Ventaja**: aprovecha mejor los datos
- **Resultado**: promedio de k evaluaciones

## 6. Flujo de Trabajo ML

```
Datos → Limpieza → Normalización → División →
Entrenamiento → Validación → Test → Predicción
```

## 7. Repositorios de Datos
- OpenML.org
- Kaggle.com
- PapersWithCode.com
- UC Irvine ML Repository
- Amazon AWS datasets

---

## Unidad 2: Reducción de Dimensionalidad

### 1. Conceptos Fundamentales

**Reducción de Dimensionalidad vs Selección de Variables:**
- **Selección**: Mantiene variables originales (ej: mantener solo "desplazamiento" y "consumo")
- **Reducción**: Crea nuevas variables transformadas (ej: PCA → "x_reducida1", "x_reducida2")

**Maldición de la Dimensionalidad:**
- **Problema**: Con muchas dimensiones, la variabilidad de distancias disminuye exponencialmente
- **Efecto**: Puntos se vuelven equidistantes → predicciones menos confiables
- **Afecta**: Algoritmos basados en distancia (k-NN, clustering, detección de anomalías)

### 2. Técnicas de Reducción

#### PCA (Principal Component Analysis)
**Concepto**: Encuentra direcciones de máxima varianza mediante factorización matricial

**Parámetros Clave:**
- **`n_components`**: Número de componentes principales
- **Escalado**: Siempre estandarizar datos (media=0, std=1)

**Propiedades:**
- Componentes **ortogonales** y **no correlacionados**
- **Orden**: λ₁ ≥ λ₂ ≥ ... ≥ λₚ (autovalores decrecientes)
- **Varianza**: Var(Yᵥ) = λᵥ (autovalor)
- **Máximo componentes**: min(n-1, p)

**Cuándo usar**: Datos lineales, preservar estructura global, interpretabilidad

#### MDS (Multidimensional Scaling)
**Concepto**: Preserva distancias entre puntos del espacio original

**Función de costo**: `C = Σ(d(xi,xj) - ||zi - zj||)²`

**Optimización**: Descenso de gradiente

#### ISOMAP
**Concepto**: MDS + distancias geodésicas (manifolds no lineales)

**Parámetros Clave:**
- **`k`**: Número de vecinos más cercanos
- **Muy pequeño k**: Grafo desconectado
- **Muy grande k**: "Atajos" incorrectos

**Algoritmo:**
1. Construir grafo k-NN
2. Calcular distancias geodésicas (Floyd-Warshall/Dijkstra)
3. Aplicar MDS clásico

**Limitaciones**: O(n³), sensible al ruido, un solo manifold conectado

#### t-SNE
**Concepto**: Preserva similitudes locales usando probabilidades

**Parámetros Clave:**
- **`perplexity`**: 5-50 (número efectivo de vecinos)
- **`n_iter`**: Número de iteraciones (≥1000)
- **`learning_rate`**: Tasa de aprendizaje
- **`early_exaggeration`**: Factor de exageración en primeras iteraciones (mejora separación inicial)

**Distribuciones:**
- **Alta dimensión**: Gaussiana con σᵢ ajustado por perplejidad
- **Baja dimensión**: t-Student (colas pesadas)

**Función de costo**: Divergencia KL: `KL(P||Q) = Σᵢ pᵢ log(pᵢ/qᵢ)`

**Características:**
- **No preserva**: Tamaños relativos de clusters, distancias globales
- **Estocástico**: Resultados varían entre ejecuciones
- **Complejidad**: O(n²) estándar, O(n log n) Barnes-Hut

#### UMAP
**Concepto**: Preserva estructura local y global usando teoría topológica

**Parámetros Clave:**
- **`n_neighbors`**: Número de vecinos
- **`min_dist`**: Distancia mínima en embedding
- **`metric`**: Métrica de distancia
- **`n_epochs`**: Número de iteraciones de optimización (afecta convergencia)

**Ventajas sobre t-SNE:**
- **Más rápido**: O(n log n)
- **Preserva estructura global** mejor
- **Determinístico** con misma semilla

### 3. Comparación de Técnicas

| Técnica | Tipo | Preserva | Complejidad | Parámetros Clave |
|---------|------|----------|-------------|------------------|
| **PCA** | Lineal | Estructura global | O(min(np², n²p)) | n_components |
| **ISOMAP** | No lineal | Distancias geodésicas | O(n³) | k (vecinos) |
| **t-SNE** | No lineal | Estructura local | O(n²) | perplexity, n_iter |
| **UMAP** | No lineal | Local + global | O(n log n) | n_neighbors, min_dist |

### 4. Consideraciones Prácticas

**Normalización**: Siempre estandarizar antes de aplicar técnicas

**Outliers**: PCA muy sensible, usar distancia de Mahalanobis para detectar

**Evaluación**:
- **PCA**: Varianza explicada acumulada
- **t-SNE/UMAP**: Múltiples ejecuciones, coherencia visual

**Elección de técnica:**
- **Datos lineales/interpretabilidad**: PCA
- **Manifolds complejos**: ISOMAP
- **Visualización clusters**: t-SNE
- **Balance velocidad/calidad**: UMAP

---

# Unidad 3: Aprendizaje No Supervisado

## 1. Conceptos Fundamentales

**Definición**: Algoritmos que buscan patrones en datos **sin variable objetivo** ni supervisión humana.

**Tipos principales**:
- **Agrupación (Clustering)**: Segmentar datos en grupos similares
- **Asociación**: Descubrir relaciones entre atributos
- **Reducción de dimensionalidad**: Simplificar datos manteniendo información relevante

---

## 2. CLUSTERING

### K-means

**Concepto**: Particiona datos en k grupos minimizando distancia intracluster.

**Asunciones importantes**:
- **Clusters esféricos** de tamaño similar
- **Variables numéricas** con distribución similar
- **Número k conocido** a priori

**Parámetros clave**:
- **`k`**: Número de clusters (crítico, debe especificarse)
- **`max_iter`**: Iteraciones máximas
- **`n_init`**: Número de inicializaciones aleatorias

**Algoritmo**:
1. Inicializar k centroides aleatoriamente
2. Asignar puntos al centroide más cercano
3. Recalcular centroides como promedio de puntos asignados
4. Repetir hasta convergencia

**Función objetivo**: Minimizar `Σ||xj - μi||²`

**Criterios de parada**:
- Centroides no cambian
- Puntos no cambian de cluster
- Límite de iteraciones alcanzado

**Selección de k**: Método del codo (RSS vs k)

### Clustering Jerárquico

**Tipos**:
- **Aglomerativo**: Bottom-up (cada punto → cluster único)
- **Divisivo**: Top-down (cluster único → puntos individuales)

**Métodos de linkage**:
- **Single**: `min(dist(Ci, Cj))` - inestable con ruido
- **Complete**: `max(dist(Ci, Cj))` - más robusto, pesimista
- **Average (UPGMA)**: promedio de distancias
- **Centroid (UPGMC)**: distancia entre centroides

**Parámetros clave**:
- **`n_clusters`**: Número final de clusters
- **`linkage`**: Método de enlace
- **`metric`**: Métrica de distancia

**Ventaja**: Genera dendrograma con jerarquía completa **Desventaja**: Algoritmos voraces (greedy), no garantizan óptimo
global

### DBSCAN

**Concepto**: Clustering basado en densidad, identifica clusters de forma arbitraria.

**Parámetros críticos**:
- **`eps`**: Radio de vecindad (debe ajustarse según escala de datos)
- **`min_samples`**: Mínimo de puntos en vecindad para ser punto central

**Tipos de puntos**:
- **Central**: ≥ min_samples puntos en radio eps
- **Frontera**: < min_samples pero al menos 1 central en vecindad
- **Ruido**: No cumple ninguna condición anterior

**Ventajas**:
- Determina automáticamente número de clusters
- Detecta formas arbitrarias
- Robusto ante outliers

**Limitaciones**:
- Sensible a parámetros eps y min_samples
- Problemas con densidades variables
- **eps debe escalarse** según unidades de los datos

### HDBSCAN

**Concepto**: Generalización jerárquica de DBSCAN.

**Parámetros clave**:
- **`min_cluster_size`**: Tamaño mínimo de cluster
- **`min_samples`**: Número mínimo de muestras

**Ventaja**: Maneja clusters de densidades variables mejor que DBSCAN

---

## 3. ASOCIACIÓN

**Objetivo**: Descubrir patrones de co-ocurrencia entre atributos.

### Algoritmo Apriori

**Parámetros**:
- **Support threshold**: Umbral de soporte mínimo
- **Confidence threshold**: Umbral de confianza

**Funcionamiento**:
1. Analizar elementos individuales y sus frecuencias
2. Generar combinaciones (itemsets) frecuentes
3. Aplicar umbral de soporte

### Eclat y FP-Growth

**Eclat**: Usa clases de equivalencia, sin generación de candidatos **FP-Growth**: Construye árbol FP, más eficiente que
Apriori

---

## 4. REDUCCIÓN DE DIMENSIONALIDAD

### PCA (Principal Component Analysis)

**Concepto**: Encuentra direcciones de máxima varianza.

**Parámetros clave**:
- **`n_components`**: Número de componentes principales
- **Escalado**: SIEMPRE estandarizar datos antes

**Propiedades**:
- Componentes ortogonales y no correlacionados
- Orden decreciente de varianza explicada
- Máximo componentes: min(n-1, p)

### t-SNE

**Concepto**: Preserva similitudes locales usando probabilidades.

**Parámetros críticos**:
- **`perplexity`**: 5-50 (número efectivo de vecinos)
- **`n_iter`**: ≥1000 iteraciones
- **`learning_rate`**: Tasa de aprendizaje

**Características**:
- Estocástico (resultados varían)
- No preserva distancias globales
- Excelente para visualización

---

## 5. VALIDACIÓN INTERNA

### Coeficiente de Silhouette

**Fórmula**: `(b-a)/max(a,b)`
- **a**: Distancia promedio intracluster
- **b**: Distancia promedio intercluster

**Interpretación**:
- **1**: Clusters bien separados
- **0**: Clusters indiferentes
- **-1**: Asignación incorrecta

### Gap Statistic

**Concepto**: Compara dispersión intracluster real vs distribución uniforme. **Uso**: Estimar número óptimo de clusters.

---

## 6. Comparación de Algoritmos

| Algoritmo | Requiere k | Forma clusters | Outliers | Parámetros |
|-----------|------------|----------------|----------|------------|
| **K-means** | Sí | Esféricos | Sensible | k |
| **Jerárquico** | Sí | Cualquiera | Moderado | n_clusters, linkage |
| **DBSCAN** | No | Arbitraria | Robusto | eps, min_samples |
| **HDBSCAN** | No | Arbitraria | Robusto | min_cluster_size |

---

# Unidad 4: Árboles de Decisión - Resumen

## 1. Conceptos Fundamentales

**Definición**: Modelo jerárquico supervisado para clasificación y regresión con alta capacidad explicativa e
interpretabilidad.

**Estructura**: Nodo raíz → Nodos internos (decisiones) → Nodos hoja (predicciones)

## 2. Algoritmos Principales

### ID3 (1986)
- **Criterio**: Entropía y ganancia de información
- **Limitación**: Solo variables categóricas

### C4.5
- **Evolución de ID3**
- **Criterio**: Ganancia de información o ratio de ganancia
- **Mejora**: Maneja variables continuas y valores faltantes

### CART (Classification And Regression Trees)
- **Criterio**: Impureza de Gini (clasificación), MSE (regresión)
- **Característica**: Árboles binarios únicamente

## 3. Parámetros Clave del Modelo

### DecisionTreeClassifier/Regressor

**`criterion`**:
- Clasificación: `'gini'`, `'entropy'`, `'log_loss'`
- Regresión: `'squared_error'`, `'absolute_error'`
- **Función**: Determina cómo medir la calidad de las divisiones

**`max_depth`**:
- **Función**: Profundidad máxima del árbol
- **Control overfitting**: Valores bajos previenen sobreajuste

**`min_samples_split`**:
- **Función**: Mínimo de muestras para dividir un nodo interno
- **Default**: 2
- **Efecto**: Valores altos reducen overfitting

**`min_samples_leaf`**:
- **Función**: Mínimo de muestras en cada hoja
- **Default**: 1
- **Efecto**: Valores altos suavizan el modelo

**`max_features`**:
- **Función**: Número máximo de variables consideradas en cada división
- **Opciones**: `'sqrt'`, `'log2'`, fracción, número entero

## 4. Criterios de Selección

### Entropía
- **Fórmula**: `H(S) = -Σ(Pi * log2(Pi))`
- **Rango**: [0,1]
- **0**: Nodo puro, **1**: Máxima impureza

### Ganancia de Información
- **Fórmula**: `Ganancia(A,S) = H(S) - H(A,S)`
- **Objetivo**: Maximizar ganancia

### Impureza de Gini
- **Fórmula**: `Gini = 1 - Σ(Pi)²`
- **Interpretación**: Probabilidad de clasificación incorrecta
- **Ventaja**: Más rápido computacionalmente que entropía

## 5. Control de Sobreajuste

### Pre-poda (Pre-pruning)
- Criterios de parada tempranos
- Parámetros: `max_depth`, `min_samples_split`, `min_samples_leaf`

### Post-poda (Post-pruning)
- Eliminar ramas que no mejoran significativamente el rendimiento
- Parámetro: `ccp_alpha` (cost complexity pruning)

## 6. Métricas de Evaluación

### Clasificación
- **Accuracy**: `(TP + TN) / (TP + TN + FP + FN)`
- **Precision**: `TP / (TP + FP)`
- **Recall**: `TP / (TP + FN)`
- **F1-score**: `2 * (Precision * Recall) / (Precision + Recall)`

### Regresión
- **MAE**: `Σ|yi - xi| / n`
- **MSE**: `Σ(yi - xi)² / n`
- **RMSE**: `√MSE`
- **R²**: Coeficiente de determinación

## 7. Ventajas y Desventajas

**Ventajas**:
- Alta interpretabilidad
- No requiere normalización
- Maneja variables categóricas y numéricas
- Robusto ante outliers

**Desventajas**:
- Propenso al overfitting
- Inestable (pequeños cambios → árboles diferentes)
- Sesgo hacia variables con más niveles
- Fronteras de decisión lineales

## 8. Casos de Uso Óptimos

- Cuando se requiere interpretabilidad
- Datos con relaciones no lineales complejas
- Variables mixtas (numéricas y categóricas)
- Como línea base para modelos ensemble

# Unidad 5: Algoritmos de Clasificación Supervisada

## 1. BAYES INGENUO (NAIVE BAYES)

### Concepto Fundamental
Algoritmo probabilístico basado en **teorema de Bayes** con **asunción de independencia condicional** entre variables.

**Fórmula**: `P(clase|datos) = P(datos|clase) × P(clase) / P(datos)`

**Clasificación**: `argmax P(c) × ∏P(di|c)` donde c es la clase y di son los atributos.

### Parámetros Clave
- **Tipo de distribución**: Determina cómo maneja variables continuas/discretas
- **Suavizado (smoothing)**: Evita probabilidades cero con técnicas como Laplace

### Tipos de Naive Bayes
1. **GaussianNB**: Variables continuas con distribución normal
2. **MultinomialNB**: Variables discretas (ej: conteo de palabras)
3. **BernoulliNB**: Variables binarias (0/1)

### Variables Continuas
- **Discretización**: Convertir en intervalos categóricos
- **Distribución Gaussiana**: `P(x|c) = (1/√2πσ²) × e^(-(x-μ)²/2σ²)`

### Ventajas y Desventajas
**Ventajas**:
- Simple y rápido
- Funciona bien con pocos datos
- Maneja alta dimensionalidad
- Escalable

**Desventajas**:
- Asunción de independencia poco realista
- Sensible a frecuencia cero
- Requiere suavizado

---

## 2. k-NN (k-NEAREST NEIGHBORS)

### Concepto Fundamental
Algoritmo **lazy learning**: no genera modelo, clasifica en tiempo de predicción basándose en **k vecinos más
cercanos**.

**Proceso**: Calcular distancias → Seleccionar k vecinos → Votación mayoritaria

### Parámetros Críticos

**`n_neighbors` (k)**:
- **Función**: Número de vecinos a considerar
- **k pequeño**: Overfitting, sensible al ruido
- **k grande**: Underfitting, clase mayoritaria domina
- **Recomendación**: Valores **impares** (evita empates), probar √n como inicio

**`metric`**: Métrica de distancia
- **Euclidiana** (p=2): `√Σ(yi-xi)²`
- **Manhattan** (p=1): `Σ|yi-xi|`
- **Minkowski**: Generalización con parámetro p

**`weights`**:
- **'uniform'**: Todos los vecinos pesan igual
- **'distance'**: Peso inversamente proporcional a distancia

**`algorithm`**: Algoritmo de búsqueda
- **'auto'**: Elige automáticamente
- **'ball_tree'**, **'kd_tree'**: Para alta dimensionalidad

### Consideraciones Importantes
- **Normalización obligatoria**: Variables en escalas comparables
- **Complejidad**: O(n) en predicción, costoso con grandes datasets
- **Maldición de dimensionalidad**: Performance se degrada con muchas dimensiones

---

## 3. SVM (SUPPORT VECTOR MACHINES)

### Concepto Fundamental
Encuentra **hiperplano óptimo** que **maximiza el margen** entre clases. Utiliza **vectores de soporte** (puntos que
definen la frontera).

**Objetivo**: Maximizar distancia mínima entre hiperplano y puntos más cercanos.

### Parámetros Críticos

**`C` (Regularización)**:
- **Función**: Controla trade-off entre margen amplio y errores de clasificación
- **C pequeño**: Margen amplio, tolerancia a errores (underfitting)
- **C grande**: Margen estrecho, poca tolerancia (overfitting)
- **Técnica**: Soft margin vs Hard margin

**`kernel`**: Función para transformar datos no lineales
- **'linear'**: `K(u,v) = u^T × v`
- **'poly'**: `K(u,v) = (γu^T×v + b)^p`
- **'rbf'** (radial): `K(u,v) = e^(-γ||u-v||²)`
- **'sigmoid'**: `K(u,v) = tanh(γu^T×v + b)`

**`gamma`** (para RBF/poly):
- **Función**: Define "alcance" de influencia de cada punto
- **Gamma alto**: Fronteras complejas, overfitting
- **Gamma bajo**: Fronteras más simples, underfitting

**`class_weight`**:
- **'balanced'**: Ajusta automáticamente pesos para datos desbalanceados
- **Función**: Ayuda con clases minoritarias

### Clasificación Multiclase
- **One-vs-One**: n(n-1)/2 clasificadores, votación
- **One-vs-All**: n clasificadores, uno por clase

### Ventajas y Desventajas
**Ventajas**:
- Efectivo en alta dimensionalidad
- Versátil con diferentes kernels
- Eficiente en memoria (solo vectores de soporte)

**Desventajas**:
- Costoso computacionalmente O(n²-n³)
- Sensible a scaling de datos
- No proporciona probabilidades directamente

---

## 4. COMPARACIÓN DE ALGORITMOS

| Algoritmo | Tipo | Interpretabilidad | Complejidad | Datos |
|-----------|------|------------------|-------------|-------|
| **Naive Bayes** | Probabilístico | Alta | Baja | Pocos datos OK |
| **k-NN** | Basado en instancias | Media | Alta predicción | Requiere muchos |
| **SVM** | Optimización | Baja | Alta entrenamiento | Funciona con pocos |

## 5. IMPLEMENTACIÓN PRÁCTICA

### Flujo de Trabajo
1. **Preprocesamiento**: Normalización (crítico para k-NN y SVM)
2. **División de datos**: Train/validation/test
3. **Búsqueda de hiperparámetros**: GridSearchCV
4. **Validación cruzada**: Para evaluar generalización
5. **Métricas**: Accuracy, precision, recall, F1-score

### Selección de Algoritmo
- **Datos categóricos + independencia**: Naive Bayes
- **Datasets pequeños + patrones locales**: k-NN
- **Alta dimensionalidad + fronteras complejas**: SVM

---

# Unidad 6: Modelos de Ensamble

## 1. Conceptos Fundamentales

**Definición**: Combinación de múltiples clasificadores para obtener mejor rendimiento que cualquier modelo individual.

**Justificación**:
- Datos insuficientes para elegir un único mejor clasificador
- Combinación redundante y complementaria mejora robustez y precisión
- Diferentes técnicas capturan diferentes patrones
- **Mayor precisión que modelos individuales**

## 2. Tipos de Ensambles

### Por Tipo de Combinación
- **Promedio**: Promedia resultados (modelos similares, poca variación)
- **Votación**: Cuenta votos de modelos (resultados muy diferentes)
- **Mezcla**: Combina resultados (resultados similares, mucha variación)

### Por Arquitectura
1. **Paralelo**: Modelos similares, mismo algoritmo, manipulación del conjunto de entrenamiento
2. **Secuencial**: Modelos diferentes, cada uno usa resultados del anterior

---

## 3. BAGGING

### Concepto
**Bootstrap Aggregating**: Genera múltiples conjuntos de entrenamiento usando **muestreo con reemplazo**.

### Algoritmo
1. **Bootstrap**: Muestreo aleatorio con reemplazo (N' = N elementos)
2. **Entrenamiento paralelo**: Cada subset entrena un clasificador independiente
3. **Agregación**: Votación mayoritaria (clasificación) o promedio (regresión)

### Parámetros Clave
- **Número de modelos**: Cantidad de clasificadores base
- **Tamaño de muestra**: Típicamente 63.25% del dataset original
- **Clasificador base**: Usualmente árboles de decisión limitados en profundidad

### Evaluación Out-of-Bag (OOB)
- **OOB samples**: ~1/3 de datos no usados en cada bootstrap
- **OOB error**: Promedio de errores en muestras no vistas
- **Ventaja**: No necesita conjunto de test separado

### Ventajas/Desventajas
**Ventajas**:
- Simple y efectivo
- Reduce varianza
- Bueno para datos de alta dimensión

**Desventajas**:
- Pérdida de interpretabilidad
- Alto costo computacional

---

## 4. RANDOM FOREST

### Concepto
**Bagging + Selección aleatoria de variables**: Combina bootstrap con selección aleatoria de atributos en cada división.

### Algoritmo
1. Bootstrap de m observaciones con reemplazo
2. En cada nodo: seleccionar n atributos aleatorios del subset
3. Construir árbol hasta máxima extensión
4. Repetir para k árboles
5. **Predicción final**: Votación mayoritaria

### Parámetros Críticos

**`n_estimators` (ntree)**:
- **Función**: Número de árboles en el bosque
- **Efecto**: Más árboles → mayor estabilidad, pero costo computacional

**`max_features` (mtry)**:
- **Función**: Número de variables candidatas en cada división
- **Opciones**: `'sqrt'`, `'log2'`, fracción, número entero
- **Efecto**: Controla diversidad vs precisión individual

**`max_depth`**:
- **Función**: Profundidad máxima de cada árbol
- **Efecto**: Controla complejidad individual de árboles

**`min_samples_split`**:
- **Función**: Mínimo de muestras para dividir nodo
- **Efecto**: Previene overfitting

**`bootstrap`**:
- **Función**: Si usar bootstrap o dataset completo
- **Default**: True

**`oob_score`**:
- **Función**: Calcular automáticamente error Out-of-Bag
- **Ventaja**: Evaluación sin conjunto de test separado

### Bias-Variance Trade-off
- **Árboles pequeños**: Bajo sesgo, alta varianza
- **Árboles complejos**: Alto sesgo, baja varianza
- **Random Forest**: Equilibra ambos mediante ensamble

### Ventajas/Desventajas
**Ventajas**:
- Alto rendimiento en datasets grandes
- Maneja muchos atributos sin selección previa
- Estima importancia de variables
- Robusto ante datos faltantes

**Desventajas**:
- Difícil interpretación
- Puede sobreajustar con ruido
- Poco control sobre el modelo

---

## 5. BOOSTING

### Concepto
**Aprendizaje secuencial**: Cada clasificador corrige errores del anterior mediante ponderación adaptativa.

### Algoritmo General
1. Entrenar clasificador débil con datos originales
2. Identificar ejemplos mal clasificados
3. **Aumentar peso** de ejemplos incorrectos
4. Entrenar siguiente clasificador con datos reponderados
5. **Combinar** todos con pesos proporcionales a precisión
6. Repetir hasta convergencia

### Tipos de Boosting

#### AdaBoost (Adaptive Boosting)
- **Método**: Ajusta pesos de datos mal clasificados
- **Objetivo**: Minimizar error de entrenamiento
- **Proceso**: Iterativo hasta obtener predictor fuerte

#### Gradient Boosting
- **Método**: Entrena sobre errores residuales del predictor anterior
- **Base**: Combina descenso de gradiente + boosting
- **Parámetros clave**: `learning_rate` (controla contribución de cada modelo)
- **Ventaja**: Más flexible que AdaBoost

#### XGBoost (Extreme Gradient Boosting)
- **Mejora**: Optimizado para velocidad y escalabilidad
- **Paralelización**: Múltiples núcleos CPU
- **Rendimiento**: Mejor que Gradient Boosting estándar

### Ventajas/Desventajas
**Ventajas**:
- Mejora precisión combinando modelos débiles
- Robusto ante overfitting
- Maneja datos desbalanceados
- Mejor interpretabilidad que otros ensambles

**Desventajas**:
- Vulnerable a outliers
- No adecuado para tiempo real
- Computacionalmente costoso

---

## 6. STACKING

### Concepto
**Meta-aprendizaje**: Usa un metamodelo para combinar predicciones de modelos base.

### Algoritmo
1. **Fase 1**: Entrenar modelos base con k-fold cross-validation
2. **Generar predicciones**: Cada fold produce predicciones out-of-fold
3. **Nuevo dataset**: Predicciones de modelos base como features
4. **Fase 2**: Entrenar metamodelo con nuevo dataset
5. **Predicción final**: Metamodelo combina predicciones de modelos base

### Características
- **Niveles múltiples**: Puede tener Level 1, Level 2, etc.
- **Metamodelo**: Aprende cómo combinar mejor las predicciones
- **Flexibilidad**: Modelos base pueden ser muy diferentes

---

## 7. COMPARACIÓN DE TÉCNICAS

| Técnica | Tipo | Entrenamiento | Fortaleza | Debilidad |
|---------|------|---------------|-----------|-----------|
| **Bagging** | Paralelo | Independiente | Reduce varianza | Poca mejora si modelos estables |
| **Random Forest** | Paralelo | Independiente + aleatoriedad | Muy robusto, maneja alta dimensión | Difícil interpretar |
| **Boosting** | Secuencial | Iterativo adaptativo | Reduce sesgo y varianza | Sensible a ruido/outliers |
| **Stacking** | Paralelo + Meta | Dos fases | Máxima flexibilidad | Complejo, riesgo overfitting |

---

## 8. Consideraciones Prácticas

### Selección de Técnica
- **Datos grandes + estabilidad**: Random Forest
- **Mejora gradual + modelos débiles**: Boosting
- **Máximo rendimiento + tiempo disponible**: Stacking
- **Baseline rápido**: Bagging

### Parámetros Críticos por Técnica
- **Random Forest**: `n_estimators`, `max_features`, `max_depth`, `oob_score`
- **Boosting**: Número de iteraciones, `learning_rate`, regularización
- **Stacking**: Elección de modelos base y metamodelo

### Evaluación
- **OOB Error**: Para Random Forest y Bagging
- **Validation Set**: Para Boosting (early stopping)
- **Cross-validation**: Para Stacking (evitar data leakage)

---

## Puntos Clave para el Examen

### Unidad 1
1. **Diferencias** entre clasificación, regresión y clustering
2. **Funciones matemáticas** de cada paradigma
3. **Importancia** de la normalización y cuándo usar cada método
4. **Propósito** de cada conjunto (train/validation/test)
5. **Ventajas** de k-fold cross-validation

### Unidad 2
1. **Maldición de dimensionalidad** y por qué afecta algoritmos basados en distancia
2. **Parámetros clave** de cada técnica y su impacto
3. **Cuándo usar** cada método según tipo de datos
4. **Diferencias** entre técnicas lineales vs no lineales
5. **Limitaciones** y complejidad computacional de cada algoritmo

### Unidad 3
1. **K-means**: Entender función objetivo, criterios de parada, selección de k, asunciones
2. **DBSCAN**: Diferencias entre puntos centrales/frontera/ruido, impacto de parámetros
3. **Clustering jerárquico**: Diferencias entre métodos de linkage
4. **Validación**: Cómo interpretar silhouette score y gap statistic
5. **Aplicaciones**: Cuándo usar cada algoritmo según características de datos

### Unidad 4
1. **Diferencias entre algoritmos**: ID3 vs C4.5 vs CART
2. **Impacto de parámetros**: Cómo `max_depth`, `min_samples_split` controlan complejidad
3. **Criterios de división**: Cuándo usar Gini vs Entropía
4. **Interpretación de métricas**: Especialmente para regresión (MSE vs MAE)
5. **Trade-off sesgo-varianza**: Parámetros para balance overfitting/underfitting

### Unidad 5
1. **Naive Bayes**: Entender asunción de independencia y manejo de variables continuas
2. **k-NN**: Impacto del valor k en bias-variance, importancia de normalización, k impar
3. **SVM**: Concepto de margen, papel del parámetro C, funciones kernel, class_weight
4. **Todos**: Cuándo usar cada algoritmo según características de datos
5. **Parámetros**: Saber qué controla cada parámetro y cómo afecta el rendimiento

### Unidad 6
1. **Conceptos**: Saber diferenciar Bagging vs Boosting vs Stacking
2. **Random Forest**: Parámetros críticos (`n_estimators`, `max_features`, `max_depth`, `oob_score`) y cómo afectan
   bias-variance
3. **Boosting**: Proceso secuencial, diferencias entre AdaBoost, Gradient Boosting y XGBoost, `learning_rate`
4. **Evaluación**: OOB error, cuándo usar cada técnica
5. **Aplicaciones**: Cuál elegir según características de datos