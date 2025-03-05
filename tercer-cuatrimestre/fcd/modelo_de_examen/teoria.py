import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Configuración visual
sns.set_theme(style="whitegrid")

# Datos de ejemplo df = pd.read_csv("datos.csv")  # Reemplazar con tus datos

# 1. DISTRIBUCIÓN DE UNA VARIABLE


# Histograma
def plot_histogram(data, variable, bins=30, kde=True):
    """
    Histograma para variables numéricas continuas

    Parámetros: - data: DataFrame - variable: str, nombre de la columna - bins: int, número de contenedores - kde: bool,
    mostrar la estimación de densidad
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x=variable, bins=bins, kde=kde)
    plt.title(f"Histograma de {variable}")
    plt.tight_layout()
    plt.show()


# Diagrama de barras
def plot_barplot(data, variable):
    """
    Diagrama de barras para variables categóricas

    Parámetros: - data: DataFrame - variable: str, nombre de la columna categórica
    """
    plt.figure(figsize=(10, 6))
    counts = data[variable].value_counts().sort_index()
    sns.barplot(x=counts.index, y=counts.values)
    plt.title(f"Diagrama de barras de {variable}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Boxplot
def plot_boxplot(data, variable, orient="v"):
    """
    Boxplot para visualizar estadísticas de posición y dispersión

    Parámetros: - data: DataFrame - variable: str, nombre de la columna numérica - orient: str, orientación ('v'
    vertical, 'h' horizontal)
    """
    plt.figure(figsize=(10, 6))
    if orient == "v":
        sns.boxplot(y=data[variable])
        plt.title(f"Boxplot de {variable}")
    else:
        sns.boxplot(x=data[variable])
        plt.title(f"Boxplot de {variable}")
    plt.tight_layout()
    plt.show()


# Gráfico de densidad
def plot_kde(data, variable):
    """
    Gráfico de densidad para estimar la distribución de probabilidad

    Parámetros: - data: DataFrame - variable: str, nombre de la columna numérica
    """
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=data, x=variable, fill=True)
    plt.title(f"Densidad de {variable}")
    plt.tight_layout()
    plt.show()


# 2. RELACIÓN ENTRE VARIABLES


# Diagrama de dispersión
def plot_scatter(data, x_var, y_var, hue=None):
    """
    Diagrama de dispersión para relación entre dos variables

    Parámetros: - data: DataFrame - x_var: str, nombre de la columna para eje X - y_var: str, nombre de la columna para
    eje Y - hue: str, opcional, nombre de la columna para color
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_var, y=y_var, hue=hue)
    plt.title(f"Dispersión entre {x_var} y {y_var}")
    plt.tight_layout()
    plt.show()


# Mapa de calor
def plot_heatmap(data, annot=True, cmap="coolwarm"):
    """
    Mapa de calor para visualizar correlaciones

    Parámetros: - data: DataFrame o matriz de correlación - annot: bool, mostrar valores - cmap: str, esquema de colores
    """
    plt.figure(figsize=(12, 10))
    corr = data.corr() if isinstance(data, pd.DataFrame) else data
    mask = np.triu(np.ones_like(corr, dtype=bool))  # Matriz triangular
    sns.heatmap(
        corr,
        mask=mask,
        annot=annot,
        cmap=cmap,
        vmin=-1,
        vmax=1,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8},
    )
    plt.title("Matriz de Correlación")
    plt.tight_layout()
    plt.show()


# Gráfico de líneas
def plot_lineplot(data, x_var, y_var, hue=None):
    """
    Gráfico de líneas para tendencias

    Parámetros: - data: DataFrame - x_var: str, nombre de la columna para eje X (típicamente tiempo) - y_var: str,
    nombre de la columna para eje Y - hue: str, opcional, nombre de la columna para color/grupos
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x=x_var, y=y_var, hue=hue, marker="o")
    plt.title(f"Tendencia de {y_var} por {x_var}")
    plt.tight_layout()
    plt.show()


# Barras agrupadas
def plot_grouped_barplot(data, x_var, y_var, hue):
    """
    Gráfico de barras agrupadas

    Parámetros: - data: DataFrame - x_var: str, categoría principal - y_var: str, variable numérica - hue: str,
    subcategoría para agrupar
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data, x=x_var, y=y_var, hue=hue)
    plt.title(f"{y_var} por {x_var} agrupado por {hue}")
    plt.legend(title=hue)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# 3. COMPOSICIÓN


# Gráfico circular (no es nativo de Seaborn, usamos matplotlib)
def plot_pie(data, variable):
    """
    Gráfico circular para proporciones

    Parámetros: - data: DataFrame - variable: str, nombre de columna categórica
    """
    plt.figure(figsize=(10, 10))
    counts = data[variable].value_counts()
    plt.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=90,
        shadow=True,
    )
    plt.axis("equal")
    plt.title(f"Distribución de {variable}")
    plt.tight_layout()
    plt.show()


# 4. COMPARACIÓN


# Gráfico de barras de error
def plot_barplot_error(data, x_var, y_var, ci=95):
    """
    Gráfico de barras con barras de error

    Parámetros: - data: DataFrame - x_var: str, categoría - y_var: str, variable numérica - ci: int, intervalo de
    confianza
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data, x=x_var, y=y_var, ci=ci)
    plt.title(f"{y_var} por {x_var} con IC {ci}%")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Violin plot
def plot_violinplot(data, x_var, y_var, hue=None, split=False):
    """
    Violin plot para comparar distribuciones

    Parámetros: - data: DataFrame - x_var: str, categoría - y_var: str, variable numérica - hue: str, opcional,
    categoría adicional - split: bool, dividir los violines si hue está presente
    """
    plt.figure(figsize=(12, 6))
    sns.violinplot(data=data, x=x_var, y=y_var, hue=hue, split=split)
    plt.title(f"Distribución de {y_var} por {x_var}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Facetas (Small multiples)
def plot_facetgrid(data, x_var, y_var, col, row=None, kind="scatter"):
    """
    Múltiples gráficos en rejilla usando FacetGrid

    Parámetros: - data: DataFrame - x_var: str, variable para eje X - y_var: str, variable para eje Y - col: str,
    variable para columnas - row: str, opcional, variable para filas - kind: str, tipo de gráfico ('scatter', 'line',
    etc.)
    """
    g = sns.FacetGrid(data, col=col, row=row, height=5, aspect=1.2)
    if kind == "scatter":
        g.map(sns.scatterplot, x_var, y_var)
    elif kind == "line":
        g.map(sns.lineplot, x_var, y_var)
    elif kind == "hist":
        g.map(sns.histplot, x_var)

    g.add_legend()
    g.fig.suptitle(f"{y_var} vs {x_var} por {col}", y=1.05)
    plt.tight_layout()
    plt.show()


# 5. ESPECÍFICOS


# Q-Q plot
def plot_qqplot(data, variable):
    """
    Q-Q plot para verificar normalidad

    Parámetros: - data: DataFrame - variable: str, nombre de columna numérica
    """
    from scipy import stats

    plt.figure(figsize=(8, 8))
    stats.probplot(data[variable].dropna(), plot=plt)
    plt.title(f"Q-Q Plot de {variable}")
    plt.tight_layout()
    plt.show()


# Gráfico de residuos (para regresión)
def plot_residuals(model, X, y):
    """
    Gráfico de residuos para modelos de regresión

    Parámetros: - model: modelo ajustado (sklearn) - X: predictores - y: variable respuesta
    """
    y_pred = model.predict(X)
    residuals = y - y_pred

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.scatter(y_pred, residuals)
    plt.axhline(y=0, color="r", linestyle="-")
    plt.xlabel("Valores predichos")
    plt.ylabel("Residuos")
    plt.title("Residuos vs Predichos")

    plt.subplot(1, 2, 2)
    sns.histplot(residuals, kde=True)
    plt.title("Distribución de residuos")

    plt.tight_layout()
    plt.show()


# Pairplot (relaciones entre múltiples variables)
def plot_pairplot(data, variables=None, hue=None, corner=True):
    """
    Matriz de dispersión entre múltiples variables

    Parámetros: - data: DataFrame - variables: list, columnas a incluir - hue: str, variable para colorear - corner:
    bool, mostrar solo el triángulo inferior
    """
    if variables:
        data_subset = data[variables]
    else:
        data_subset = data

    g = sns.pairplot(data, vars=variables, hue=hue, corner=corner)
    g.fig.suptitle("Relaciones entre variables", y=1.02)
    plt.tight_layout()
    plt.show()


# Ejemplo de uso plot_histogram(df, 'peso_kg_bebe') plot_scatter(df, 'semanas_gest', 'peso_kg_bebe') plot_heatmap(df)
