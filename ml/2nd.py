import pandas as pd

# Sample car data
data = {
    'Make': ['Toyota', 'Honda', 'Ford', 'BMW', 'Tesla'],
    'Model': ['Corolla', 'Civic', 'F-150', '3 Series', 'Model 3'],
    'Year': [2020, 2019, 2021, 2018, 2022],
    'Mileage_km': [35000, 40000, 25000, 50000, 10000],
    'Fuel_Type': ['Petrol', 'Petrol', 'Diesel', 'Diesel', 'Electric'],
    'Price_USD': [15000, 14000, 28000, 22000, 45000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('car_dataset.csv', index=False)

print("Car dataset saved to 'car_dataset.csv'")
