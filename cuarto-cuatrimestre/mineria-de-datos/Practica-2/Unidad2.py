# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:54:17 2023

@author: flavio
"""
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE, Isomap
from sklearn.decomposition import PCA
from umap import UMAP

target_names = {
    1:'Kama',
    2:'Rosa', 
    3:'Canadian'
}

dataWheat = pd.read_csv("wheat.csv")
dataWheat['category'] = dataWheat['category'].map(target_names)

xWheat = dataWheat.drop('category', axis=1)
yWheat = dataWheat['category']

sns.countplot(
    x='category', 
    data=dataWheat)
plt.title('Wheat targets value count')
plt.show()

xWheatScaled = StandardScaler().fit_transform(xWheat)

""" PCA """

pca = PCA(n_components=3)
 
pcaFeatures = pca.fit_transform(xWheatScaled)
 
print('Shape before PCA: ', xWheatScaled.shape)
print('Shape after PCA: ', pcaFeatures.shape)
 
pcaWheat = pd.DataFrame(
    data=pcaFeatures, 
    columns=['PC1', 'PC2', 'PC3'])

pcaWheat['category'] = yWheat.to_numpy()
 
pcaWheat
	
pca.explained_variance_

pca.singular_values_

# Bar plot of explained_variance
plt.bar(
    range(1,len(pca.explained_variance_)+1), pca.explained_variance_)
 
plt.plot(
    range(1,len(pca.explained_variance_ )+1),
    np.cumsum(pca.explained_variance_),
    c='red',
    label='Cumulative Explained Variance')
 
plt.legend(loc='upper left')
plt.xlabel('Number of components')
plt.ylabel('Explained variance (eignenvalues)')
plt.title('Scree plot')
 
plt.show()

sns.set()
sns.lmplot(
    x='PC1', 
    y='PC2', 
    data=pcaWheat, 
    hue='category', 
    fit_reg=False, 
    legend=True
    )
 
plt.title('2D PCA Graph')
plt.show()

""" Isomap """

isomapWheat = Isomap(n_neighbors=6, n_components=2)
isomapWheat.fit(xWheatScaled)
manifold_2Da = isomapWheat.transform(xWheatScaled)
manifold_2D = pd.DataFrame(manifold_2Da, columns=['Component 1', 'Component 2'])
manifold_2D['category'] = yWheat.to_numpy()

groups = manifold_2D.groupby('category')
plt.title('2D Isomap Graph')
for name, group in groups:
    plt.plot(group['Component 1'], group['Component 2'], marker='o', linestyle='', markersize=5, label=name)
plt.legend()

# Left with 2 dimensions
manifold_2D.head()

""" t-SNE """

time_start = time.time()
tsneWheat = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
tsneWheatResults = tsneWheat.fit_transform(xWheatScaled)

print('t-SNE done! Time elapsed: {} seconds'.format(time.time()-time_start))

subsetWheatTSNE = pd.DataFrame(yWheat)
subsetWheatTSNE['tsne-2d-one'] = tsneWheatResults[:,0]
subsetWheatTSNE['tsne-2d-two'] = tsneWheatResults[:,1]

plt.figure(figsize=(16,10))
sns.scatterplot(
    x="tsne-2d-one", y="tsne-2d-two",
    hue="category",
    palette=sns.color_palette("hls", 15),
    data=subsetWheatTSNE,
    legend="full",
    alpha=0.8
)

""" UMAP """

umap_2d = UMAP(n_components=2, init='random', random_state=0)
umap_3d = UMAP(n_components=3, init='random', random_state=0)

proj_2d = umap_2d.fit_transform(xWheat)

umapProj2D = pd.DataFrame(proj_2d, columns=['Component 1', 'Component 2'])
umapProj2D['category'] = yWheat.to_numpy()

groups = umapProj2D.groupby('category')
plt.title('2D Unamp Graph')
for name, group in groups:
    plt.plot(group['Component 1'], group['Component 2'], marker='o', linestyle='', markersize=5, label=name)
plt.legend()

proj_3d = umap_3d.fit_transform(xWheat)
umapProj3D = pd.DataFrame(proj_3d, columns=['Component 1', 'Component 2', 'Component 3'])
umapProj3D['category'] = yWheat.to_numpy()

# axes instance
fig = plt.figure(figsize=(10, 6))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# find all the unique labels in the 'name' column
labels = np.unique(umapProj3D['category'])
# get palette from seaborn
palette = sns.color_palette("husl", len(labels))

# plot
for label, color in zip(labels, palette):
    df1 = umapProj3D[umapProj3D['category'] == label]
    ax.scatter(df1['Component 1'], df1['Component 2'], df1['Component 3'],
               s=40, marker='o', color=color, alpha=1, label=label)
ax.set_xlabel('Component 1')
ax.set_ylabel('Component 2')
ax.set_zlabel('Component 3')

# legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()