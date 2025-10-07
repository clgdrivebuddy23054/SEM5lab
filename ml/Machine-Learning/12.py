# Import necessary libraries
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Step 1: Generate simple 2D binary classification data
X, y = make_classification(n_samples=100, n_features=2, 
                           n_redundant=0, n_informative=2,
                           n_clusters_per_class=1, random_state=42)

# Step 2: Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

# Step 3: Create mesh grid for decision boundary plot
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Step 4: Plot the decision boundary and data points
plt.figure(figsize=(8, 6))
cmap_bg = ListedColormap(['#FFCCCC', '#CCCCFF'])  # Background colors
cmap_pts = ListedColormap(['#FF0000', '#0000FF'])  # Point colors

plt.contourf(xx, yy, Z, cmap=cmap_bg, alpha=0.6)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_pts, edgecolor='k', s=60)
plt.title('Random Forest Classification (Binary)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()
