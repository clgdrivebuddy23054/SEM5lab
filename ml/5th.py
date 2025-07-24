import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# 1. Generate synthetic dataset
np.random.seed(42)
X = np.random.normal(0, 1, (100, 2))
X[:10] += 10  # Add outliers
y = X[:, 0] * 2 + np.random.normal(0, 0.1, 100)  # target with noise

# 2. Detect outliers
iso_forest = IsolationForest(contamination=0.1)
outlier_flags = iso_forest.fit_predict(X)

# 3. Remove outliers
mask = outlier_flags == 1
X_clean = X[mask]
y_clean = y[mask]

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_clean, y_clean, test_size=0.2, random_state=42)

# 5. Train a regression model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# 6. Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (after outlier removal): {mse:.4f}")

# Optional: Plot before and after outlier removal
plt.scatter(X[:, 0], X[:, 1], c=outlier_flags, cmap='coolwarm', label='Outliers=Red')
plt.title('Outlier Detection with Isolation Forest')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
