import pandas as pd
import numpy as np

# Step 1: Load the dirty data
raw_df = pd.read_csv('aircraft_bigdata_dirty.csv')

# Step 2: Data Cleaning
clean_df = raw_df.copy()

# Clean 'Type' column: fix typos and fill missing
clean_df['Type'] = clean_df['Type'].replace({'A32O': 'A320', 'B73seven': 'B737', '': np.nan})
clean_df['Type'].fillna('Unknown', inplace=True)

# Clean 'Manufacturer' column: fix typos and fill missing
clean_df['Manufacturer'] = clean_df['Manufacturer'].replace({'Airbuss': 'Airbus', 'Boieng': 'Boeing', None: np.nan})
clean_df['Manufacturer'].fillna('Unknown', inplace=True)

# Clean 'Capacity' column: convert to numeric, handle errors, fill missing/invalid
clean_df['Capacity'] = pd.to_numeric(clean_df['Capacity'], errors='coerce')
median_capacity = clean_df['Capacity'].median()
clean_df['Capacity'].fillna(median_capacity, inplace=True)

# Clean 'Range_km' column: convert to numeric, handle errors, fill missing/invalid
clean_df['Range_km'] = pd.to_numeric(clean_df['Range_km'], errors='coerce')
mean_range = clean_df['Range_km'].mean()
clean_df['Range_km'].fillna(mean_range, inplace=True)

# Clean 'Status' column: standardize values
clean_df['Status'] = clean_df['Status'].str.strip().str.title()
clean_df['Status'] = clean_df['Status'].replace({
    'In Service': 'Active',
    'Out Of Service': 'Retired',
    'Active': 'Active',
    'Retired': 'Retired'
})
clean_df['Status'].fillna('Unknown', inplace=True)

# Step 3: Basic Analysis
summary = clean_df.groupby('Manufacturer').agg({
    'AircraftID': 'count',
    'Capacity': 'mean',
    'Range_km': 'mean'
}).rename(columns={'AircraftID': 'NumAircraft', 'Capacity': 'AvgCapacity', 'Range_km': 'AvgRange_km'})

print('Summary by Manufacturer:')
print(summary)

# Step 4: Export cleaned data for Power BI
clean_df.to_csv('aircraft_bigdata_cleaned.csv', index=False)
print('\nCleaned data exported to aircraft_bigdata_cleaned.csv') 