from sklearn.datasets import make_classification
import pandas as pd

# Step 1: Create synthetic data
X, y = make_classification(
    n_samples=1000,       # number of data points
    n_features=10,        # total number of features
    n_informative=5,      # number of informative features
    n_redundant=2,        # number of redundant features
    n_classes=2,          # binary classification (0 or 1)
    random_state=42       # seed for reproducibility
)

# Step 2: Convert to pandas DataFrame
feature_names = [f'feature_{i}' for i in range(X.shape[1])]
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# Step 3: Save dataset to a CSV file
df.to_csv('synthetic_classification_dataset.csv', index=False)

print("Dataset created and saved as 'synthetic_classification_dataset.csv'")
