from sklearn.linear_model import LinearRegression
import numpy as np

# Sample training data
# X: input feature (e.g., years of experience)
# y: target output (e.g., salary)
X = np.array([[1], [2], [3], [4], [5]])  # input feature
y = np.array([10000, 20000, 30000, 40000, 50000])  # target variable

# Create the model
model = LinearRegression()

# Train (fit) the model
model.fit(X, y)

# Predict using the trained model
predictions = model.predict(X)

# Display results
print("Original Input (X):")
print(X)
print("\nActual Output (y):")
print(y)
print("\nPredicted Output:")
print(predictions)

# Print the model parameters
print("\nModel Coefficient (slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)
