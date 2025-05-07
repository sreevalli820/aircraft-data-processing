import pandas as pd
import numpy as np
import random

# Seed for reproducibility
np.random.seed(42)
random.seed(42)

num_rows = 2000

types = ['A320', 'B737', 'A380', 'B747', 'B777', 'A350', 'B787']
manufacturers = ['Airbus', 'Boeing', 'Airbus', 'Boeing', 'Airbus', 'Boeing']
statuses = ['Active', 'Retired', 'active', 'retired', 'In Service', 'Out of Service']

data = []
for i in range(1, num_rows + 1):
    row = {
        'AircraftID': i,
        'Type': random.choice(types + ['A32O', 'B73seven']),  # Add some typos
        'Manufacturer': random.choice(manufacturers + ['Airbuss', 'Boieng']),  # Add some typos
        'Year': random.choice(range(1990, 2023)),
        'Capacity': random.choice([random.randint(120, 550), '', None, 'unknown']),  # Missing/invalid
        'Range_km': random.choice([random.randint(5000, 16000), '', None, 'n/a']),  # Missing/invalid
        'Status': random.choice(statuses)
    }
    # Randomly introduce missing values
    if random.random() < 0.05:
        row['Type'] = ''
    if random.random() < 0.05:
        row['Manufacturer'] = None
    data.append(row)

df = pd.DataFrame(data)
df.to_csv('aircraft_bigdata_dirty.csv', index=False)
print('Generated aircraft_bigdata_dirty.csv with 2000 rows and data issues.') 