import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Sample skewed data
data = {
    'Income': [1000, 1200, 1500, 2000, 3000, 5000, 10000, 25000, 50000, 100000]
}
df = pd.DataFrame(data)
print("Original Data:\n", df)

# Step 2: Apply log transformation to normalize
df['Log_Income'] = np.log(df['Income'])

print("\nAfter Log Transformation:\n", df)

# Step 3: Plot before and after
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
sns.histplot(df['Income'], kde=True, bins=10)
plt.title("Original (Skewed)")

plt.subplot(1, 2, 2)
sns.histplot(df['Log_Income'], kde=True, bins=10)
plt.title("Log Transformed (More Normal)")

plt.tight_layout()
plt.show()
