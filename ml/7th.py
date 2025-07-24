import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Sample data: rows = samples, columns = features
data = np.array([
    [1.0, 200.0, 5000.0],
    [2.0, 300.0, 7000.0],
    [3.0, 400.0, 9000.0],
    [4.0, 500.0, 11000.0]
])

print("Original Data:\n", data)

# 1. Standardization (mean = 0, std = 1)
standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(data)
print("\nStandard Scaled Data:\n", standard_scaled)

# 2. Normalization to [0, 1]
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(data)
print("\nMin-Max Scaled Data:\n", minmax_scaled)

# 3. Robust Scaling (uses median and IQR)
robust_scaler = RobustScaler()
robust_scaled = robust_scaler.fit_transform(data)
print("\nRobust Scaled Data:\n", robust_scaled)
