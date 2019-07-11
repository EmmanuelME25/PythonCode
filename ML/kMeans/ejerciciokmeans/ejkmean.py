import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat

import modulo
from modulo import * 

data_imagen = loadmat('data/bird_small_kmeans.mat')
A=data_imagen['A']
A.shape

A=A/255.
X=np.reshape(A,(A.shape[0]*A.shape[1],A.shape[2]))
initial_centroids=init_centroids(X,16)
idx,centroids=run_K_means(X,initial_centroids,10)
idx=find_closest_centroids(X,centroids)
x_recovered=centroids[idx.astype(int),:]

plt.imshow(x_recovered)
plt.savefig('pajaro_c.png')



data= loadmat('data/clustering_colors.mat')
X=data['X']

initial_centroids = initial_centroids= np.array([[3,3],[6,2],[8,5]])

idx = find_closest_centroids(X, initial_centroids)
print(idx[0:500])

modulo.compute_centroids(X,idx,3)

idx,centroids= run_K_means(X,initial_centroids,10)
print (centroids)

cluster1 = X[np.where(idx == 0)[0],:]
cluster2 = X[np.where(idx == 1)[0],:]
cluster3 = X[np.where(idx == 2)[0],:]

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3')
ax.legend()

plt.xlabel('Diferencia de temperatura')
plt.ylabel('Diferencia de presion')
plt.savefig("kmeans_reloaded.pdf")

