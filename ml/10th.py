import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate synthetic regression data
X, y = make_regression(n_samples=200, n_features=1, noise=10.0, random_state=42)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree Regressor
regressor = DecisionTreeRegressor(max_depth=4, random_state=42)
regressor.fit(X_train, y_train)

# Predict on test data
y_pred = regressor.predict(X_test)

# Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Plot the regression tree
plt.figure(figsize=(12, 6))
plot_tree(regressor, filled=True, feature_names=["Feature 1"])
plt.title("Decision Tree Regressor")
plt.show()

# Visualize prediction results
X_grid = np.linspace(X.min(), X.max(), 500).reshape(-1, 1)
y_grid_pred = regressor.predict(X_grid)

plt.figure(figsize=(10, 5))
plt.scatter(X, y, color="lightgray", label="Original Data")
plt.plot(X_grid, y_grid_pred, color="red", label="Regression Tree Prediction")
plt.title("Decision Tree Regression")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
plt.grid(True)
plt.show()
