# SE Weekly assignment by Kshitiz Sachan

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# Set the latitude and longitude of the location
latitude = 37.7749
longitude = -122.4194

# Set your API key
api_key = "YOUR_API_KEY"

# Make the API request
url = f"https://api.openei.org/utility_rates?version=latest&lat={latitude}&lon={longitude}&format=json&api_key={api_key}"
response = requests.get(url)
data = json.loads(response.text)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data["items"])

# Convert the start and end dates to datetime objects
df["startdate"] = pd.to_datetime(df["startdate"])
df["enddate"] = pd.to_datetime(df["enddate"])

# Calculate the duration of each rate plan
df["duration"] = (df["enddate"] - df["startdate"]).dt.days

# Plot the duration of each rate plan
plt.bar(df["label"], df["duration"])
plt.xticks(rotation=90)
plt.ylabel("Duration (days)")
plt.show()
