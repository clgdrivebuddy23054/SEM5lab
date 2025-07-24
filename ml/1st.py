import numpy as np
import pandas as pd
from sklearn.datasets import make_classification

# Parameters
n_samples = 1000  # Number of rows in the dataset
n_features = 10   # Number of input features
n_classes = 2     # Binary classification

# Generate the dataset
X, y = make_classification(n_samples=n_samples, 
                           n_features=n_features, 
                           n_informative=5, 
                           n_redundant=2, 
                           n_classes=n_classes, 
                           random_state=42)

# Create a DataFrame
feature_columns = [f"feature_{i+1}" for i in range(n_features)]
df = pd.DataFrame(X, columns=feature_columns)
df['target'] = y

# Save to CSV
df.to_csv('synthetic_classification_dataset.csv', index=False)

print("Dataset created and saved as 'synthetic_classification_dataset.csv'")
