# DVA-Project
Team 169
NY weather csv data source: climate.gov https://www.climate.gov/maps-data/dataset/past-weather-zip-code-data-table
NY weather data description: GHCND_documentation.pdf

# Data Munging 
Run this code block first before the subsequent ones:
## Method 1: Using `munge_df()`
```python
from batch.munge_df import munge_df

import pandas as pd

df = pd.read_csv("data/Motor_Vehicle_Collisions_-_Crashes.csv")

df = munge_df(df)
```

## Method 2: Manually

```python
import pandas as pd

df = pd.read_csv("data/Motor_Vehicle_Collisions_-_Crashes.csv")
# Replace column name spaces with underscore
df.columns = df.columns.str.replace(" ", "_")

# Link weather station
df_nearest = pd.read_csv("data/weather_station_mapping.csv")

df = df.merge(
    df_nearest,
    left_on=["LATITUDE", "LONGITUDE"],
    right_on=["LATITUDE_ACCIDENT", "LONGITUDE_ACCIDENT"],
    how="left",
    validate="m:1",
)

df_null_zip = pd.read_csv("data/imputed_zip.csv")

# Link missing zipcodes (only if lat/lon is present)
df = df.merge(df_null_zip, on=["LATITUDE", "LONGITUDE"], how="left", validate="m:1")

df["ZIP_CODE"] = np.where(
    df["ZIP_CODE"].isnull(), df["ZIP_CODE_IMPUTED"], df["ZIP_CODE"]
)
```