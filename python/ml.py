# K-Means Clustering on Iris Dataset

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Convert into DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)

print("First 5 rows of Iris Dataset:")
print(df.head())

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------------
# Elbow Method
# -------------------------------

inertia = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot Elbow Curve
plt.figure(figsize=(7, 5))
plt.plot(range(2, 11), inertia, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.grid(True)
plt.show()

# -------------------------------
# Silhouette Score
# -------------------------------

silhouette_scores = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, labels)
    silhouette_scores.append(score)

# Display silhouette scores
print("\nSilhouette Scores:")

for k, score in zip(range(2, 11), silhouette_scores):
    print("K =", k, "Score =", round(score, 3))

# Find best K
best_k = range(2, 11)[silhouette_scores.index(max(silhouette_scores))]

print("\nBest number of clusters:", best_k)

# -------------------------------
# Final K-Means Model
# -------------------------------

kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

df["Cluster"] = clusters

print("\nClustered Data:")
print(df.head(10))

# -------------------------------
# Visualize Clusters
# -------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=clusters,
    s=50
)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering of Iris Dataset")
plt.grid(True)
plt.show()