# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Step 1: Create sample data
X, _ = make_blobs(n_samples=30, centers=3, random_state=42)

# Step 2: Perform hierarchical clustering
linked = linkage(X, method='ward')  # "ward" minimizes variance

# Step 3: Plot dendrogram
plt.figure(figsize=(8, 4))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Dendrogram (Hierarchical Clustering)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.grid(True)
plt.show()

# Step 4: Assign clusters from dendrogram (cut at 3 clusters)
clusters = fcluster(linked, t=3, criterion='maxclust')

# Step 5: Plot clustered data
plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='Set1', edgecolor='k', s=100)
plt.title('Hierarchical Clustering Result')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()
