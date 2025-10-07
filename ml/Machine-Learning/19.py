import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Step 1: Load dataset (Iris dataset for example)
data = load_iris()
X = data.data  # shape = (150, 4)

# Step 2: Standardize the data (zero mean and unit variance)
X_meaned = X - np.mean(X, axis=0)

# Step 3: Compute covariance matrix
cov_matrix = np.cov(X_meaned, rowvar=False)

# Step 4: Compute eigenvalues and eigenvectors
eigen_values, eigen_vectors = np.linalg.eigh(cov_matrix)

# Step 5: Sort eigenvalues and corresponding eigenvectors in descending order
sorted_indices = np.argsort(eigen_values)[::-1]
eigen_values = eigen_values[sorted_indices]
eigen_vectors = eigen_vectors[:, sorted_indices]

# Step 6: Select top k eigenvectors (e.g., 2 for visualization)
k = 2
eigenvector_subset = eigen_vectors[:, 0:k]

# Step 7: Transform data
X_reduced = np.dot(X_meaned, eigenvector_subset)

# Step 8: Visualize
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=data.target, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA - Iris Dataset')
plt.colorbar(label='Target Class')
plt.show()
