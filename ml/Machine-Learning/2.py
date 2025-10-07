import pandas as pd

# ----------------------
# WRITE DATASET TO CSV
# ----------------------

# Sample data: dictionary of lists
data = {
    'feature1': [1.5, 2.3, 3.1],
    'feature2': [0, 1, 0],
    'target':   [1, 0, 1]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Write to CSV file
df.to_csv('2_sample_dataset.csv', index=False)
print("✅ Dataset written to 'sample_dataset.csv'")

# ----------------------
# READ DATASET FROM CSV
#
# Read the dataset from CSV
read_df = pd.read_csv('2_sample_dataset.csv')

# Show contents
print("\n✅ Dataset read from 'sample_dataset.csv':")
print(read_df)

