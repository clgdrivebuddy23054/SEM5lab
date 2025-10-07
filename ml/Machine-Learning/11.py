# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Step 1: Load the Iris dataset (only 2 features for easy plotting)
iris = load_iris()
X = iris.data[:, :2]  # Only the first two features (sepal length & sepal width)
y = iris.target

# Step 2: Train the Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X, y)

# Step 3: Create a mesh grid for plotting decision boundaries
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Step 4: Plot the decision boundaries and data points
plt.figure(figsize=(8, 6))
cmap = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
plt.contourf(xx, yy, Z, cmap=cmap)

# Plot actual data points
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap=ListedColormap(['#FF0000', '#00FF00', '#0000FF']))
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Decision Tree Classification (Iris Dataset)')
plt.grid(True)
plt.show()
