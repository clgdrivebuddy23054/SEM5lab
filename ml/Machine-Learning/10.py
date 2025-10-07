# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# Step 1: Create simple training data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])  # Input feature
y = np.array([1.5, 1.7, 3.2, 3.9, 5.1, 5.5, 6.8, 7.5, 8.8, 9.6])  # Output values

# Step 2: Create and train the Decision Tree Regressor
model = DecisionTreeRegressor()
model.fit(X, y)

# Step 3: Predict values for a smooth curve
X_test = np.linspace(1, 10, 100).reshape(-1, 1)
y_pred = model.predict(X_test)

# Step 4: Plot the original data and prediction
plt.scatter(X, y, color='red', label='Actual Data')          # Red dots: actual data
plt.plot(X_test, y_pred, color='blue', label='Prediction')   # Blue line: prediction
plt.title('Decision Tree Regression')
plt.xlabel('X values')
plt.ylabel('Predicted y values')
plt.legend()
plt.grid(True)
plt.show()
