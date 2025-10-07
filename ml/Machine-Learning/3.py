import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# ------------------------
# Step 1: Create sample data with missing values
# ------------------------
data = {
    'feature1': [1.2, 2.4, np.nan, 4.5, 5.1],
    'feature2': [3.3, np.nan, 1.1, 4.4, np.nan],
    'target':   [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print("Original dataset with missing values:\n", df)

# ------------------------
# Step 2: Impute missing values
# ------------------------

# Create an imputer that replaces missing values with the mean
imputer = SimpleImputer(strategy='mean')

# Apply imputer to feature columns only
df[['feature1', 'feature2']] = imputer.fit_transform(df[['feature1', 'feature2']])

print("\nDataset after imputation:\n", df)
