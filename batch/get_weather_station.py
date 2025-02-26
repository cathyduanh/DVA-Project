# %%
import glob
import geopandas
import pandas as pd

###########################
# IMPORT DATA
###########################
# Get NYC df
df = pd.read_csv("data/Motor_Vehicle_Collisions_-_Crashes.csv")
# Replace column name spaces with underscore
df.columns = df.columns.str.replace(" ", "_")
# Filter null coordinates
df = df[~df["LOCATION"].isnull()]
# Remove duplicates
df = df[~df["LOCATION"].duplicated()][["LATITUDE", "LONGITUDE"]].reset_index(drop=True)

# Get weather station df
files = glob.glob("data/NY Weather*.csv")
df_weather = pd.concat([pd.read_csv(file) for file in files])

# Remove duplicates
df_weather = df_weather[~df_weather[["LATITUDE", "LONGITUDE"]].duplicated()][
    ["STATION", "LATITUDE", "LONGITUDE"]
].reset_index(drop=True)

###########################
# CREATE MAPPING CSV
###########################
# %%
gdf = geopandas.GeoDataFrame(
    df,
    geometry=geopandas.points_from_xy(df["LATITUDE"], df["LONGITUDE"]),
)
gdf_weather = geopandas.GeoDataFrame(
    df_weather,
    geometry=geopandas.points_from_xy(df_weather["LATITUDE"], df_weather["LONGITUDE"]),
)

df_nearest = geopandas.sjoin_nearest(
    gdf,
    gdf_weather,
    distance_col="DISTANCE_FROM_WEATHER_STATION",
    lsuffix="ACCIDENT",
    rsuffix="WEATHER_STATION",
)
df_neareset = df_nearest.drop(columns=["geometry", "index_WEATHER_STATION"])

# Save mapping to csv
df_nearest.to_csv("data/weather_station_mapping.csv", index=False)
# %%

###########################
# MERGE NEAREST WEATHER STATION
###########################
df = pd.read_csv("data/Motor_Vehicle_Collisions_-_Crashes.csv")

df.merge(
    df_nearest,
    left_on=["LATITUDE", "LONGITUDE"],
    right_on=["LATITUDE_ACCIDENT", "LONGITUDE_ACCIDENT"],
    how="left",
    validate="m:1",
)

# %%
