from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture
from sklearn.datasets import load_iris

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
dataset = load_iris()

X = pd.DataFrame(dataset.data)
X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']

y = pd.DataFrame(dataset.target)
y.columns = ['Targets']

# Plot setup
plt.figure(figsize=(14, 7))
colormap = np.array(['red', 'lime', 'black'])

# Real data plot
plt.subplot(1, 3, 1)
plt.scatter(
    X.Petal_Length,
    X.Petal_Width,
    c=colormap[y.Targets],
    s=40
)
plt.title('Real')

# K-Means clustering
plt.subplot(1, 3, 2)

model = KMeans(n_clusters=3, random_state=0, n_init=10)
model.fit(X)

predY = model.labels_

plt.scatter(
    X.Petal_Length,
    X.Petal_Width,
    c=colormap[predY],
    s=40
)
plt.title('KMeans')

# GMM (EM Algorithm)
scaler = preprocessing.StandardScaler()
X_scaled = scaler.fit_transform(X)

gmm = GaussianMixture(n_components=3, random_state=0)
gmm.fit(X_scaled)

y_cluster_gmm = gmm.predict(X_scaled)

plt.subplot(1, 3, 3)
plt.scatter(
    X.Petal_Length,
    X.Petal_Width,
    c=colormap[y_cluster_gmm],
    s=40
)
plt.title('GMM Classification')

plt.tight_layout()
plt.show()
