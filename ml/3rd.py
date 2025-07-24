import pandas as pd

# --- Step 1: Create and write the dataset ---
car_data = {
    'Make': ['Toyota', 'Honda', 'Ford', 'BMW', 'Tesla'],
    'Model': ['Corolla', 'Civic', 'F-150', '3 Series', 'Model 3'],
    'Year': [2020, 2019, 2021, 2018, 2022],
    'Mileage_km': [35000, 40000, 25000, 50000, 10000],
    'Fuel_Type': ['Petrol', 'Petrol', 'Diesel', 'Diesel', 'Electric'],
    'Price_USD': [15000, 14000, 28000, 22000, 45000]
}

# Convert to DataFrame
df = pd.DataFrame(car_data)

# Save to CSV file
csv_filename = 'car_dataset.csv'
df.to_csv(csv_filename, index=False)
print(f"✅ Dataset written to '{csv_filename}'")

# --- Step 2: Read the dataset back ---
df_read = pd.read_csv(csv_filename)

# Show the data
print("\n📄 Dataset read from file:")
print(df_read)
