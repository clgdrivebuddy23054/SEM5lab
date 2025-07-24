import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample Data (X = feature, y = target)
X = np.array([[1], [2], [3], [4], [5]])  # 2D array: n_samples x n_features
y = np.array([3, 5, 7, 9, 11])           # Target values

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Model parameters
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict new values
X_new = np.array([[6], [7]])
y_pred = model.predict(X_new)
print("Predictions for 6 and 7:", y_pred)

# Plot data and regression line
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, model.predict(X), color='red', label='Regression line')
plt.scatter(X_new, y_pred, color='green', marker='x', label='Predictions')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
