import pandas as pd  
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt 

# load dataset
iris = load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)

# apply kmeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
x['cluster'] = kmeans.fit_predict(x)

# reduce dimensions to 2 using PCA for plotting
# pca used to reduce the dimensions (features combine not removed)
pca = PCA(n_components=2)
components = pca.fit_transform(x[iris.feature_names])

# plot clusters
plt.figure(figsize=(8,6))
plt.scatter(components[:, 0], components[:, 1], c=x['cluster'], cmap='viridis')
plt.title('Flower clusters found by kmeans(Unsupervised)')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.colorbar(label= 'Cluster Group')
plt.tight_layout()
plt.show()

# x-axis : components[:, 0] - all rows but 1st column
# y-axis : components[:, 1] - 