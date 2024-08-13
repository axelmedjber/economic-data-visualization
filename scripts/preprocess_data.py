import requests
import pandas as pd
import io

# Define the URL for the data
data_url = 'https://sdmx.oecd.org/public/rest/data/OECD.ECO.MAD,DSD_EO@DF_EO,1.1/.GDPV_ANNPCT.A?startPeriod=2021&dimensionAtObservation=AllDimensions'

# Send a request to the URL
response = requests.get(data_url)

# Check if the request was successful
if response.status_code == 200:
    # Decode the content to string
    content = response.content.decode('utf-8')

    # Convert the content to a pandas DataFrame
    data = pd.read_csv(io.StringIO(content))

    # Display the first few rows
    print(data.head())

    # Save the raw data to a CSV file
    data.to_csv('../economic-data-visualization/data/raw_oecd_gdp_data.csv', index=False)
    print("Data saved to '../economic-data-visualization/data/raw_oecd_gdp_data.csv'")
else:
    print(f"Failed to retrieve data: {response.status_code}")

# Preprocess the data
# Example preprocessing steps
# Remove any rows with missing values
data.dropna(inplace=True)

# Convert the 'TIME_PERIOD' column to datetime format if it exists
if 'TIME_PERIOD' in data.columns:
    data['TIME_PERIOD'] = pd.to_datetime(data['TIME_PERIOD'])

# Filter for specific countries or regions if needed
# data = data[data['LOCATION'].isin(['USA', 'CAN', 'FRA'])]

# Save the cleaned data
data.to_csv('../economic-data-visualization/data/cleaned_oecd_gdp_data.csv', index=False)
print("Cleaned data saved to '../economic-data-visualization/data/cleaned_oecd_gdp_data.csv'")
