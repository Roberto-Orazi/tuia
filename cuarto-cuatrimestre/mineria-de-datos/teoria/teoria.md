# Análisis de Datos Agrícolas: Explicación del Código

## 1. Configuración Inicial

```python
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 12
```

- **Propósito**: Establecer estilo visual coherente para todas las gráficas
- **Función**: Mejora legibilidad con fondo cuadriculado, tamaño adecuado y fuente legible
- **Importancia**: Facilita interpretación visual de resultados

## 2. Análisis Exploratorio de Datos (EDA)

### 2.1 Histogramas

```python
for i, columna in enumerate(columnas_numericas):
    sns.histplot(data=df_cultivos, x=columna, kde=True, ax=axes[i], color='skyblue')
```

- **Propósito**: Visualizar distribución de variables numéricas
- **Función**: Muestra frecuencia de valores y forma de distribución
- **Hallazgos clave**:
  - Variables con distribución normal (temperatura, humedad)
  - Distribuciones bimodales (nitrógeno, fósforo)
  - Distribución sesgada (potasio)

### 2.2 Boxplots Generales

```python
for i, columna in enumerate(columnas_numericas):
    sns.boxplot(x=df_cultivos[columna], ax=axes[i], color='lightgreen')
```

- **Propósito**: Identificar outliers y visualizar estadísticos principales
- **Función**: Muestra mediana, cuartiles y valores atípicos
- **Utilidad**: Detecta potasio como variable con numerosos outliers

### 2.3 Boxplots por Tipo de Cultivo

```python
for i, columna in enumerate(columnas_numericas):
    sns.boxplot(x='tipoCultivo', y=columna, data=df_cultivos, ax=axes[i],
                hue='tipoCultivo', palette='Set2', legend=False)
```

- **Propósito**: Comparar distribuciones entre diferentes cultivos
- **Función**: Revela patrones específicos por tipo de cultivo
- **Hallazgos**:
  - Maíz/Arroz tienen mayor contenido de nitrógeno
  - Algodón presenta niveles más altos de potasio

### 2.4 Gráficos de Violín

```python
for i, columna in enumerate(columnas_numericas):
    sns.violinplot(x='tipoCultivo', y=columna, data=df_cultivos, ax=axes[i],
                   hue='tipoCultivo', palette='Set3', inner='quartile', legend=False)
```

- **Propósito**: Visualizar distribución completa por cultivo
- **Función**: Combina boxplot con estimación de densidad
- **Ventaja**: Revela distribuciones multimodales dentro de cada cultivo

### 2.5 Matriz de Correlación

```python
correlation_matrix = df_cultivos[columnas_numericas].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
```

- **Propósito**: Identificar relaciones lineales entre variables
- **Función**: Muestra coeficientes de correlación de Pearson
- **Hallazgos clave**:
  - Correlación positiva temperatura-humedad (+0.53)
  - Correlación negativa nitrógeno-fósforo (-0.64)
  - Correlación negativa nitrógeno-potasio (-0.45)

### 2.6 Pairplot (Scatterplot Matricial)

```python
sns.pairplot(df_cultivos[columnas_numericas + ['tipoCultivo']], hue='tipoCultivo',
             diag_kind='kde', plot_kws={'alpha': 0.6})
```

- **Propósito**: Visualizar relaciones bivariadas entre todas las variables
- **Función**: Facilita detección de clusters y tendencias
- **Utilidad**: Confirma visualmente correlaciones identificadas

## 3. Tratamiento de Outliers

```python
bigotes_cultivo = {}
for cultivo in df_cultivos['tipoCultivo'].unique():
   datos_cultivo = df_cultivos[df_cultivos['tipoCultivo'] == cultivo]['potasio']
   q1 = datos_cultivo.quantile(0.25)
   q3 = datos_cultivo.quantile(0.75)
   riq = q3 - q1
   bigote_superior = q3 + 1.5 * riq
   bigotes_cultivo[cultivo] = bigote_superior

media_bigotes_superiores = sum(bigotes_cultivo.values()) / len(bigotes_cultivo)
df_sin_outliers = df_cultivos[df_cultivos['potasio'] <= media_bigotes_superiores].copy()
```

- **Propósito**: Eliminar valores atípicos que distorsionan análisis
- **Método**: Usa criterio de Tukey (Q3 + 1.5*IQR) para identificar outliers
- **Estrategia**: Calcula límite promedio entre cultivos para preservar diferencias naturales
- **Importancia**: Mejora robustez de análisis posteriores

## 4. Preprocesamiento para Análisis Avanzado

```python
# Codificación de variables categóricas
for col in columnas_categoricas:
   le = LabelEncoder()
   df_sin_outliers[f"{col}_encoded"] = le.fit_transform(df_sin_outliers[col])

# Normalización
scaler = StandardScaler()
df_escalado = pd.DataFrame(
    scaler.fit_transform(df_sin_outliers[todas_columnas_para_escalar]),
    columns=[f"{col}_norm" for col in todas_columnas_para_escalar],
    index=df_sin_outliers.index
)
```

- **Propósito**: Preparar datos para algoritmos sensibles a escala
- **Procedimientos**:
  - Codificación de variables categóricas a numéricas
  - Estandarización a media 0 y desviación estándar 1
- **Importancia**: Evita que variables con mayor magnitud dominen análisis

## 5. Reducción de Dimensionalidad

### 5.1 PCA (Análisis de Componentes Principales)

```python
pca = PCA(n_components=df_escalado.shape[1])
pca_features = pca.fit_transform(df_escalado)
```

- **Propósito**: Reducir dimensionalidad preservando máxima varianza
- **Funcionamiento**: Crea combinaciones lineales de variables originales
- **Ventajas**:
  - Reduce ruido en datos
  - Facilita visualización en 2D/3D
  - Elimina multicolinealidad

### 5.2 Análisis de Varianza Explicada

```python
varianza_explicada = pca.explained_variance_ratio_
plt.bar(range(1, n_componentes + 1), pca.explained_variance_ratio_)
plt.step(range(1, n_componentes + 1), np.cumsum(pca.explained_variance_ratio_))
```

- **Propósito**: Determinar componentes óptimos a conservar
- **Visualizaciones**:
  - Gráfico de barras: contribución de cada componente
  - Gráfico de sedimentación: punto de inflexión para selección
  - Curva acumulativa: porcentaje total de varianza explicada
- **Utilidad**: Balance entre reducción y conservación de información

### 5.3 Visualización PCA

```python
# 2D PCA plot
plt.figure(figsize=(12, 8))
for cultivo in unique_cultivos:
    mask = pca_df["tipoCultivo"] == cultivo
    plt.scatter(pca_features[mask, 0], pca_features[mask, 1],
                color=cultivo_color_map[cultivo], label=cultivo, alpha=0.7)
```

- **Propósito**: Representar datos en espacio reducido
- **Función**: Permite visualizar agrupaciones naturales
- **Interpretación**: Evalúa separabilidad entre cultivos

### 5.4 T-SNE (t-Distributed Stochastic Neighbor Embedding)

```python
perplexity_list = [5, 30, 50, 100]
for i, perplexity in enumerate(perplexity_list):
    tsne = TSNE(n_components=2, perplexity=perplexity, max_iter=1000, random_state=42)
    tsne_result = tsne.fit_transform(X_pca)
```

- **Propósito**: Reducción no lineal que preserva estructura local
- **Exploración**: Prueba diferentes valores de perplejidad
- **Ventaja**: Mejor separación de clusters que PCA para relaciones no lineales

### 5.5 ISOMAP

```python
n_neighbors_list = [5, 15, 30, 50, 100, 200]
for i, n_neighbors in enumerate(n_neighbors_list):
    isomap = Isomap(n_neighbors=n_neighbors, n_components=2)
    isomap_result = isomap.fit_transform(X)
```

- **Propósito**: Preservar distancias geodésicas entre puntos
- **Exploración**: Diferentes configuraciones de vecindad
- **Aplicación**: Útil para datos en variedades no lineales (manifolds)

## 6. Análisis de Clustering

### 6.1 K-means con Evaluación de Número Óptimo

```python
range_n_clusters = range(2, 11)
for n_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X)
    silhouette_avg = silhouette_score(X, cluster_labels)
    silhouette_scores.append(silhouette_avg)
    inertia.append(kmeans.inertia_)
```

- **Propósito**: Agrupar cultivos basados en similitud multivariada
- **Métodos de evaluación**:
  - Silhouette score: calidad y cohesión de clusters
  - Método del codo: punto de inflexión en inercia
- **Utilidad**: Determina número óptimo de agrupaciones

### 6.2 Visualización de Clusters

```python
# 3D visualization with cluster centers
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')
for i in range(n_clusters):
    mask = cluster_labels == i
    ax.scatter(features_for_viz[mask, 0], features_for_viz[mask, 1], features_for_viz[mask, 2],
               s=30, alpha=0.3, c=[colors[i]])
ax.scatter(centers_pca[:, 0], centers_pca[:, 1], centers_pca[:, 2],
           s=200, marker='X', c=colors[:n_clusters], edgecolors='k', linewidths=2)
```

- **Propósito**: Representar grupos y centros en espacio 3D
- **Función**: Facilita interpretación visual de estructura
- **Elementos**:
  - Puntos coloreados por cluster
  - Centros marcados con X grande
  - Proyección en componentes principales

### 6.3 GAP Statistic

```python
def gap_statistic(data, k_max=10, n_refs=5):
    # [...código de implementación...]
    return k_max
```

- **Propósito**: Método avanzado para determinar número óptimo de clusters
- **Funcionamiento**: Compara agrupación con datos de referencia uniforme
- **Ventaja**: Validación estadística más robusta que métodos visuales

## 7. Conclusiones del Análisis

El análisis progresivo desde técnicas exploratorias hasta métodos avanzados permite:

1. **Caracterizar variables**: Identificar distribuciones y outliers
2. **Detectar patrones**: Correlaciones entre variables y agrupaciones naturales
3. **Reducir dimensionalidad**: Visualizar estructura compleja en espacios manejables
4. **Agrupar cultivos**: Identificar similitudes basadas en múltiples variables

Esta metodología integral proporciona insights importantes sobre los patrones de cultivo y requerimientos nutricionales,
potencialmente útiles para optimización agrícola.