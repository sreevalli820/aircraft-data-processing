# Aircraft Data Processing

The project contains scripts for generating and processing aircraft data. It includes functionality to create sample datasets with realistic data issues for testing data cleaning and processing workflows.

## Features

- Generate sample aircraft data with common data quality issues
- Includes typos, missing values, and inconsistent formatting
- Configurable number of records
- Reproducible results with fixed random seeds

## Setup

1. Clone the repository
2. Install required packages:
   ```bash
   pip install pandas numpy
   ```

## Usage

To generate sample data:
```bash
python generate_aircraft_bigdata_dirty.py
```

This will create a CSV file with 2000 rows of aircraft data containing various data quality issues.

## Overview
This project is designed for data analyst interview preparation. It demonstrates how to process, clean, and analyze aircraft data using Python, with the output ready for integration with Power BI. The script is beginner-friendly and well-commented for easy understanding.

## What the Script Does
- **Generates a sample aircraft dataset** with fields like AircraftID, Type, Manufacturer, Year, Capacity, Range (km), and Status.
- **Introduces missing values** to simulate real-world data issues.
- **Cleans the data** by filling missing values with appropriate statistics (median or mean).
- **Performs basic analysis** by summarizing the number of aircraft, average capacity, and average range by manufacturer.
- **Exports the cleaned data** to a CSV file (`cleaned_aircraft_data.csv`) for easy use in Power BI or other tools.

## How to Run the Script
1. Make sure you have Python installed (version 3.7 or higher recommended).
2. Install the required packages:
   ```bash
   pip install pandas numpy
   ```
3. Run the script:
   ```bash
   python aircraft_data_processing.py
   ```
4. The script will print a summary analysis and create a file called `cleaned_aircraft_data.csv` in the same directory.

## Data Fields
- **AircraftID:** Unique identifier for each aircraft
- **Type:** Model/type of the aircraft (e.g., A320, B737)
- **Manufacturer:** Company that made the aircraft (e.g., Airbus, Boeing)
- **Year:** Year of manufacture
- **Capacity:** Number of passengers the aircraft can carry
- **Range_km:** Maximum range in kilometers
- **Status:** Whether the aircraft is Active or Retired

## Analysis Performed
The script groups the data by manufacturer and calculates:
- Number of aircraft
- Average capacity
- Average range (km)

This summary is printed to the console for quick insights.

## Power BI Integration
The exported `cleaned_aircraft_data.csv` can be directly imported into Power BI for further visualization and dashboard creation. You can create charts such as:
- Number of aircraft by manufacturer
- Average capacity by manufacturer
- Trends in aircraft types or years

## Customization
You can easily modify the script to:
- Add more aircraft records
- Introduce new fields (e.g., country, airline)
- Perform more advanced analyses

---

**This project is a great starting point for data analysts to practice data cleaning, analysis, and preparing data for business intelligence tools like Power BI.** 