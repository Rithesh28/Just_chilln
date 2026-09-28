# Hierarchical Agglomerative Clustering
# Using Iris Dataset

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Load Iris dataset
iris = load_iris()

X = iris.data

# Create DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)

print("First 5 rows of Iris Dataset:")
print(df.head())

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --------------------------------
# Create Dendrogram
# --------------------------------

linked = linkage(X_scaled, method='ward')

plt.figure(figsize=(12, 6))

dendrogram(
    linked,
    truncate_mode='lastp',
    p=20
)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")

plt.show()

# --------------------------------
# Agglomerative Clustering
# --------------------------------

model = AgglomerativeClustering(
    n_clusters=3,
    linkage='ward'
)

clusters = model.fit_predict(X_scaled)

# Add cluster labels
df["Cluster"] = clusters

print("\nClustered Data:")
print(df.head(10))

# Display cluster counts
print("\nNumber of data points in each cluster:")
print(df["Cluster"].value_counts().sort_index())

# --------------------------------
# Visualize Clusters
# --------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=clusters,
    s=50
)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Hierarchical Agglomerative Clustering")
plt.grid(True)

plt.show()