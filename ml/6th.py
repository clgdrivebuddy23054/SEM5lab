import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import PowerTransformer

# Generate non-normal data (exponential distribution)
np.random.seed(42)
data = np.random.exponential(scale=2.0, size=1000)
df = pd.DataFrame({'non_normal': data})

# Visualize original distribution
sns.histplot(df['non_normal'], kde=True, color='red')
plt.title("Original Non-Normal Distribution")
plt.show()

# === 1. Log Transform ===
df['log_transformed'] = np.log1p(df['non_normal'])

# === 2. Power Transform (Yeo-Johnson) ===
pt = PowerTransformer(method='yeo-johnson')
df['yeojohnson'] = pt.fit_transform(df[['non_normal']])

# Visualize Transformed Distributions
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.histplot(df['log_transformed'], kde=True, ax=axes[0], color='blue')
axes[0].set_title("Log Transformed")

sns.histplot(df['yeojohnson'], kde=True, ax=axes[1], color='green')
axes[1].set_title("Yeo-Johnson Transformed")

plt.tight_layout()
plt.show()
