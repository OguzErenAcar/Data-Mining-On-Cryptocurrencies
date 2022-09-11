# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

plt.style.use("ggplot")

#----------------kasim-----------------------#
dataset = pd.read_csv("kasim_binance.csv")
X=dataset.iloc[:,[14,15]].values

x_kripto_isimler_kasim=dataset.iloc[:,[0]].values

##ELBOW METOD
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method (kasım)')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(X)

# kriptoların isimlerinin consola yazılması
# count=0;
# kumeler_kasim=[[],[],[]]
#
# for t in range(3):
#     for j in X[y_kmeans==t,0]:
#         for i in x_kripto_isimler_kasim:
#            if(dataset.iloc[count,14]==j):
#                 kumeler_kasim[t].append(i[0])
#            count=count+1
#         count=0;
#     print("küme ", t + 1, "oluştu..")
#
# print("kümeleniyor...")
#
# matris=np.array([kumeler_kasim[0],kumeler_kasim[1],kumeler_kasim[2]] ,dtype=object)
# print(matris)
#

plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=50,c='orange',label='Cluster1',alpha=0.8)
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=50,c='blue',label='Cluster2',alpha=0.8)
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=50,c='lime',label='Cluster3',alpha=0.8)

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=50,c='yellow',label='Centroids')

plt.title('Kripto Kümeleri (kasim)')
plt.xlabel('Volume fark')
plt.ylabel('Fiyat fark ')
plt.legend()
plt.show()


#----------------ekim-----------------------#

dataset2 = pd.read_csv("ekim_binance.csv")
X2=dataset2.iloc[:,[14,15]].values

##ELBOW METOD
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(X2)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method (ekim)')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

x_kripto_isimler_ekim=dataset2.iloc[:,[0]].values

kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
y2_kmeans=kmeans.fit_predict(X2)
#
# kriptoların isimlerinin consola yazılması
# count2=0;
# kumeler_ekim=[[],[],[]]
#
#
# for t in range(3):
#      for j in X2[y2_kmeans==t,0]:
#         for i in x_kripto_isimler_ekim:
#            if(dataset2.iloc[count2,14]==j):
#                 kumeler_ekim[t].append(i[0])
#            count2=count2+1
#         count2=0
#      print("küme ", t + 1, "oluştu..")
#
#
# print("kümeleniyor...")
#
# matris2=np.array([kumeler_ekim[0],kumeler_ekim[1],kumeler_ekim[2]] ,dtype=object)
# print(matris2)


plt.scatter(X2[y2_kmeans==0,0],X2[y2_kmeans==0,1],s=50,c='orange',label='Cluster1',alpha=0.8)
plt.scatter(X2[y2_kmeans==1,0],X2[y2_kmeans==1,1],s=50,c='lime',label='Cluster2',alpha=0.8)
plt.scatter(X2[y2_kmeans==2,0],X2[y2_kmeans==2,1],s=50,c='blue',label='Cluster3',alpha=0.8)

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=50,c='yellow',label='Centroids')

plt.title('Clusters of crypto(ekim)')
plt.xlabel('volume fark')
plt.ylabel('fiyat fark ')
plt.legend()
plt.show()


# #----------------2 ay da ortak kriptoların bulunması-----------------------#
# dizi_index=[0,2,1]
# for i in range(3):
#     for j in kumeler_ekim[i]:
#         for k in kumeler_kasim[dizi_index[i]]:
#             if j[:-2]==k[:-2]:
#                 print(j, end="   ")
#
#     print("")
