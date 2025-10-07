import pandas as pd

# Sample data with an outlier
data = {
    'Age': [25, 26, 24, 28, 27, 26, 100]  # 100 is an outlier
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original Data:\n", df)

# Step 1: Calculate Q1, Q3, and IQR
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

# Step 2: Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Step 3: Remove outliers
df_no_outliers = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]

print("\nData after removing outliers:\n", df_no_outliers)
