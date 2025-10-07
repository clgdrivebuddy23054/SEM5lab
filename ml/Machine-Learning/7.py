import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Example dataset (rows are samples, columns are features)
data = np.array([
    [1.0, 200.0, 3000.0],
    [2.0, 190.0, 3200.0],
    [3.0, 210.0, 3100.0],
    [4.0, 220.0, 3300.0]
])

def scale_data(data, method='standard'):
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    elif method == 'robust':
        scaler = RobustScaler()
    else:
        raise ValueError(f"Unknown method: {method}")

    scaled_data = scaler.fit_transform(data)
    return scaled_data

# Choose scaling method: 'standard', 'minmax', or 'robust'
method = 'standard'
scaled = scale_data(data, method)

print(f"Original Data:\n{data}")
print(f"\nScaled Data ({method}):\n{scaled}")
