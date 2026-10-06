#EM & K-Means Algorithm

from sklearn.cluster import KMeans 
from sklearn import preprocessing 
from sklearn.mixture import GaussianMixture 
from sklearn.datasets import load_iris 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

dataset = load_iris() 
X = pd.DataFrame(dataset.data) 
X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'] 
y = pd.DataFrame(dataset.target) 
y.columns = ['Targets'] 

plt.figure(figsize=(14, 7)) 
colormap = np.array(['red', 'lime', 'black']) 

#Real
plt.subplot(1, 3, 1) 
plt.scatter(X.Petal_Length, X.Petal_Width, 
            c=colormap[y.Targets], s=40) 
plt.title('Real') 
plt.subplot(1, 3, 2) 

#KMM
model = KMeans(n_clusters=3) 
model.fit(X) 
predY = np.choose(model.labels_, [0, 1, 2]).astype(np.int64) 

plt.scatter(X.Petal_Length, X.Petal_Width, 
            c=colormap[predY], s=40) 
plt.title('KMeans') 

#GMM(EM)
scaler = preprocessing.StandardScaler() 
X_scaled = scaler.fit_transform(X) 
gmm = GaussianMixture(n_components=3) 
gmm.fit(X_scaled) 
y_cluster_gmm = gmm.predict(X_scaled) 
plt.subplot(1, 3, 3) 
plt.scatter(X.Petal_Length, X.Petal_Width, 
            c=colormap[y_cluster_gmm], s=40) 
plt.title('GMM Classification') 
plt.show() 
