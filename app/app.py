import requests
import pandas as pd
from io import StringIO

# Define the URL for data query
data_url = 'https://sdmx.oecd.org/public/rest/data/OECD.ECO.MAD,DSD_EO@DF_EO,1.1/.GDPV_ANNPCT.A?startPeriod=2021&dimensionAtObservation=AllDimensions'

# Send a request to the URL
response = requests.get(data_url)

# Check if request was successful
if response.status_code == 200:
    data = response.text
    print("Data fetched successfully!")
else:
    print("Failed to retrieve data")

# Convert the data to a DataFrame
# Note: SDMX data is often in XML format, so you'll need to parse it accordingly
# For this example, let's assume it's in a CSV format for simplicity

# Convert text to StringIO object
data_io = StringIO(data)

# Read data into DataFrame
df = pd.read_csv(data_io)
print(df.head())
