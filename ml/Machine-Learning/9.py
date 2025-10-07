from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample binary classification data
# X: input features (e.g., hours studied)
# y: labels (0 = Fail, 1 = Pass)
X = np.array([[1], [2], [3], [4], [5], [6], [7]])
y = np.array([0, 0, 0, 1, 1, 1, 1])

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Predict labels
predictions = model.predict(X)

# Predict probabilities
probabilities = model.predict_proba(X)

# Display results
print("Input (Hours Studied):")
print(X.flatten())

print("\nActual Labels (0=Fail, 1=Pass):")
print(y)

print("\nPredicted Labels:")
print(predictions)

print("\nPredicted Probabilities (Fail / Pass):")
print(probabilities)
