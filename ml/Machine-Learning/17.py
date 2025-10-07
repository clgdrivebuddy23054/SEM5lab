import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# K-Means algorithm
def k_means(X, k, max_iters=100):
    # Step 1: Initialize centroids randomly
    np.random.seed(42)
    centroids = X[np.random.choice(len(X), k, replace=False)]

    for i in range(max_iters):
        # Step 2: Assign clusters
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        cluster_labels = np.argmin(distances, axis=1)

        # Step 3: Update centroids
        new_centroids = np.array([X[cluster_labels == j].mean(axis=0) for j in range(k)])

        # Step 4: Check for convergence
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, cluster_labels

# Run K-means
k = 4
centroids, labels = k_means(X, k)

# Plot result
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.show()
