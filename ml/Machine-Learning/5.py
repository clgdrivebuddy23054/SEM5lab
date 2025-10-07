import pandas as pd

# Step 1: Sample data
data = {
    'Marks': [45, 67, 89, 56, 77, 90, 34, 49]
}
df = pd.DataFrame(data)
print("Original Data:\n", df)

# Step 2: Perform binning (3 bins: Low, Medium, High)
bins = [0, 50, 75, 100]
labels = ['Low', 'Medium', 'High']

df['Marks_Binned'] = pd.cut(df['Marks'], bins=bins, labels=labels)

print("\nAfter Binning:\n", df)
