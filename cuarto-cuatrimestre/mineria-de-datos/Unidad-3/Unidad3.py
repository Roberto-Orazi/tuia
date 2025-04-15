# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:06:51 2023

@author: flavio
"""
OMP_NUM_THREADS=1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from gap_statistic import OptimalK

target_names = {
    1:'Kama',
    2:'Rosa', 
    3:'Canadian'
}

dataWheat = pd.read_csv("wheat.csv")
dataWheat['category'] = dataWheat['category'].map(target_names)

xWheat = np.array(dataWheat[["area","length","asymmetry coefficient"]])
yWheat = np.array(dataWheat['category'])

# axes instance
fig = plt.figure(figsize=(10, 6))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

labels = np.unique(dataWheat['category'])
palette = sns.color_palette("husl", len(labels))

# plot
for label, color in zip(labels, palette):
    df1 = dataWheat[dataWheat['category'] == label]
    ax.scatter(df1['area'], df1['length'], df1['asymmetry coefficient'],
               s=40, marker='o', color=color, alpha=1, label=label)
ax.set_xlabel('area')
ax.set_ylabel('length')
ax.set_zlabel('asymmetry coefficient')

""" K-means """

Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
score = [kmeans[i].fit(xWheat).score(xWheat) for i in range(len(kmeans))]

plt.plot(Nc,score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()

kmeans = KMeans(n_clusters=5).fit(xWheat)
centroids = kmeans.cluster_centers_
print(centroids)

# Getting the cluster centers
centerClusters = kmeans.cluster_centers_

fig = plt.figure(figsize=(10, 6))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

dataWheat['newClass'] = kmeans.predict(xWheat)
labels = np.unique(dataWheat['newClass'])
palette = sns.color_palette("husl", len(labels))

# plot
for label, color in zip(labels, palette):
    df1 = dataWheat[dataWheat['newClass'] == label]
    ax.scatter(df1['area'], df1['length'], df1['asymmetry coefficient'],
               s=40, marker='o', color=color, alpha=1, label=label)
    ax.scatter(centerClusters[:, 0], centerClusters[:, 1], centerClusters[:, 2], 
               marker='*', color=color, s=200)
ax.set_xlabel('area')
ax.set_ylabel('length')
ax.set_zlabel('asymmetry coefficient')

gs_obj = OptimalK(n_jobs=1, n_iter= 10)
n_clusters = gs_obj(xWheat, n_refs=50, cluster_array=np.arange(1, 15))
print('Optimal number of clusters: ', n_clusters)

""" Clustering Jerárquico """

xCustomers = pd.read_csv('Mall_Customers.csv')
miniCustomers = xCustomers.iloc[:, [2, 3]].values

# Creamos el dendograma para encontrar el número óptimo de clusters
dendrogram = sch.dendrogram(sch.linkage(miniCustomers, method = 'ward'))
plt.title('Dendograma')
plt.xlabel('Categorias')
plt.ylabel('Distancias Euclidianas')
plt.show()

# Ajustando Clustering Jerárquico al conjunto de datos
hc = AgglomerativeClustering(n_clusters = 4, 
                    metric= 'euclidean', 
                    linkage = 'ward')

y_hc = hc.fit_predict(miniCustomers)
print(f'Silhouette Score(n=4): {silhouette_score(miniCustomers, y_hc)}')

# Visualising the clusters
plt.scatter(miniCustomers[y_hc == 0, 0], miniCustomers[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(miniCustomers[y_hc == 1, 0], miniCustomers[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(miniCustomers[y_hc == 2, 0], miniCustomers[y_hc == 2, 1], s = 100, c = 'black', label = 'Cluster 3')
plt.scatter(miniCustomers[y_hc == 3, 0], miniCustomers[y_hc == 3, 1], s = 100, c = 'grey', label = 'Cluster 4')
plt.title('Clusters of customers')
plt.xlabel('Perimeter')
plt.ylabel('Category')
plt.legend()
plt.show()

gs_obj = OptimalK(n_jobs=1, n_iter=20)
n_clusters = gs_obj(miniCustomers.astype('float'), n_refs=60, cluster_array=np.arange(2, 10))
print('Optimal number of clusters: ', n_clusters)

""" DBSCAN """

xCustomers = xCustomers[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

clustering = DBSCAN(eps=12.5, min_samples=4).fit(xCustomers)
DBSCAN_dataset = xCustomers.copy()
DBSCAN_dataset.loc[:,'Cluster'] = clustering.labels_ 

DBSCAN_dataset.Cluster.value_counts().to_frame()

outliers = DBSCAN_dataset[DBSCAN_dataset['Cluster']==-1]

fig2, (axes) = plt.subplots(1,2,figsize=(12,5))

sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)',
                data=DBSCAN_dataset[DBSCAN_dataset['Cluster']!=-1],
                hue='Cluster', ax=axes[0], palette='Set2', legend='full', s=200)

sns.scatterplot(x='Age', y='Spending Score (1-100)',
                data=DBSCAN_dataset[DBSCAN_dataset['Cluster']!=-1],
                hue='Cluster', palette='Set2', ax=axes[1], legend='full', s=200)

axes[0].scatter(outliers['Annual Income (k$)'], outliers['Spending Score (1-100)'], s=10, label='outliers', c="k")

axes[1].scatter(outliers['Age'], outliers['Spending Score (1-100)'], s=10, label='outliers', c="k")
axes[0].legend()
axes[1].legend()

plt.setp(axes[0].get_legend().get_texts(), fontsize='12')
plt.setp(axes[1].get_legend().get_texts(), fontsize='12')
plt.show()

https://www.kaggle.com/code/amanrosekaursethi/crop-analysis-clustering-and-prediction