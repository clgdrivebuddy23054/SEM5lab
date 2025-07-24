import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# --- Step 1: Create a sample dataset with missing values ---
data = {
    'Make': ['Toyota', 'Honda', 'Ford', 'BMW', np.nan],
    'Year': [2020, 2019, np.nan, 2018, 2022],
    'Mileage_km': [35000, np.nan, 25000, 50000, 10000],
    'Fuel_Type': ['Petrol', 'Petrol', 'Diesel', np.nan, 'Electric']
}

df = pd.DataFrame(data)

print("🔍 Original Data with Missing Values:")
print(df)

# --- Step 2: Impute missing values ---

# Impute numeric columns with the mean
num_cols = ['Year', 'Mileage_km']
imputer_num = SimpleImputer(strategy='mean')
df[num_cols] = imputer_num.fit_transform(df[num_cols])

# Impute categorical columns with the most frequent (mode)
cat_cols = ['Make', 'Fuel_Type']
imputer_cat = SimpleImputer(strategy='most_frequent')
df[cat_cols] = imputer_cat.fit_transform(df[cat_cols])

print("\n✅ Data After Imputation:")
print(df)
