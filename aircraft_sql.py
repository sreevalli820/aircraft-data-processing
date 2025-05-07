import sqlite3
import pandas as pd
import numpy as np

# Step 1: Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')

# Step 2: Create the aircraft table
conn.execute('''
CREATE TABLE aircraft (
    AircraftID INTEGER,
    Type TEXT,
    Manufacturer TEXT,
    Year INTEGER,
    Capacity TEXT,
    Range_km TEXT,
    Status TEXT
)
''')

# Step 3: Insert sample data (with some issues)
sample_data = [
    (1, 'A320', 'Airbus', 2010, '180', '6100', 'Active'),
    (2, 'B737', 'Boeing', 2012, '160', '5600', 'Active'),
    (3, 'A32O', 'Airbuss', 2011, '', '6100', 'active'),  # Typos, missing capacity, lowercase status
    (4, 'B747', 'Boeing', 2005, '416', 'n/a', 'Retired'), # 'n/a' in range
    (5, '', None, 2013, 'unknown', '5600', 'In Service'), # Missing type/manufacturer, 'unknown' capacity
    (6, 'A380', 'Airbus', 2018, '525', '15200', 'Active'),
    (7, 'B777', 'Boieng', 2015, '396', '', 'Out of Service'), # Typo in manufacturer, missing range
]
conn.executemany('INSERT INTO aircraft VALUES (?, ?, ?, ?, ?, ?, ?)', sample_data)

# Step 4: Load data into pandas DataFrame
df = pd.read_sql_query('SELECT * FROM aircraft', conn)

# Step 5: Data Cleaning (same as before)
df['Type'] = df['Type'].replace({'A32O': 'A320', 'B73seven': 'B737', '': np.nan})
df['Type'].fillna('Unknown', inplace=True)
df['Manufacturer'] = df['Manufacturer'].replace({'Airbuss': 'Airbus', 'Boieng': 'Boeing', None: np.nan})
df['Manufacturer'].fillna('Unknown', inplace=True)
df['Capacity'] = pd.to_numeric(df['Capacity'], errors='coerce')
median_capacity = df['Capacity'].median()
df['Capacity'].fillna(median_capacity, inplace=True)
df['Range_km'] = pd.to_numeric(df['Range_km'], errors='coerce')
mean_range = df['Range_km'].mean()
df['Range_km'].fillna(mean_range, inplace=True)
df['Status'] = df['Status'].str.strip().str.title()
df['Status'] = df['Status'].replace({
    'In Service': 'Active',
    'Out Of Service': 'Retired',
    'Active': 'Active',
    'Retired': 'Retired'
})
df['Status'].fillna('Unknown', inplace=True)

# Step 6: Basic Analysis
summary = df.groupby('Manufacturer').agg({
    'AircraftID': 'count',
    'Capacity': 'mean',
    'Range_km': 'mean'
}).rename(columns={'AircraftID': 'NumAircraft', 'Capacity': 'AvgCapacity', 'Range_km': 'AvgRange_km'})

print('Summary by Manufacturer:')
print(summary)

# Step 7: Export cleaned data to CSV
df.to_csv('aircraft_sql_cleaned.csv', index=False)
print('\nCleaned data exported to aircraft_sql_cleaned.csv') 