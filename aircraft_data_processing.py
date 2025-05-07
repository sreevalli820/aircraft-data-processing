import pandas as pd
import numpy as np

# Step 1: Generate a sample aircraft dataset
data = {
    'AircraftID': range(1, 11),
    'Type': ['A320', 'B737', 'A320', 'B747', 'B737', 'A380', 'A320', 'B777', 'A350', 'B787'],
    'Manufacturer': ['Airbus', 'Boeing', 'Airbus', 'Boeing', 'Boeing', 'Airbus', 'Airbus', 'Boeing', 'Airbus', 'Boeing'],
    'Year': [2010, 2012, 2011, 2005, 2013, 2018, 2010, 2015, 2017, 2016],
    'Capacity': [180, 160, 180, 416, 160, 525, 180, 396, 315, 242],
    'Range_km': [6100, 5600, 6100, 13800, 5600, 15200, 6100, 15600, 15000, 14140],
    'Status': ['Active', 'Active', 'Active', 'Retired', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active']
}
df = pd.DataFrame(data)

# Step 2: Introduce some missing values for realism
df.loc[3, 'Capacity'] = np.nan  # B747 missing capacity
df.loc[7, 'Range_km'] = np.nan  # B777 missing range

# Step 3: Data Cleaning
# Fill missing Capacity with median
median_capacity = df['Capacity'].median()
df['Capacity'].fillna(median_capacity, inplace=True)
# Fill missing Range_km with mean
mean_range = df['Range_km'].mean()
df['Range_km'].fillna(mean_range, inplace=True)
df['Range_km'] = df['Range_km'].astype(int)

# Step 4: Basic Analysis
summary = df.groupby('Manufacturer').agg({
    'AircraftID': 'count',
    'Capacity': 'mean',
    'Range_km': 'mean'
}).rename(columns={'AircraftID': 'NumAircraft', 'Capacity': 'AvgCapacity', 'Range_km': 'AvgRange_km'})

print('Summary by Manufacturer:')
print(summary)

# Step 5: Export cleaned data for Power BI
df.to_csv('cleaned_aircraft_data.csv', index=False)
print('\nCleaned data exported to cleaned_aircraft_data.csv') 