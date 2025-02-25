# %%
import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from tqdm.auto import tqdm

tqdm.pandas()
# %%
###########################
# IMPORT DATA
###########################
df = pd.read_csv("data/Motor_Vehicle_Collisions_-_Crashes.csv")
# df = df.head(20)
# Replace column name spaces with underscore
df.columns = df.columns.str.replace(" ", "_")

# Filter data with known lat/lon but with null zip codes
df_null_zip = df[
    (~df[["LATITUDE", "LONGITUDE"]].isnull().all(axis=1)) & (df["ZIP_CODE"].isnull())
].copy()

print(f"There are {df_null_zip.shape[0]} rows with lat/lon and null zip codes")

df_null_zip["LAT_LON"] = (
    df_null_zip["LATITUDE"].astype(str) + ", " + df_null_zip["LONGITUDE"].astype(str)
)

# %%
############################
# REVERSE ZIP CODE LOOKUP
############################
geolocator = Nominatim(user_agent="reverse_geocoding")
reverse_geocode = RateLimiter(geolocator.reverse, min_delay_seconds=2)

# Keep lookup in memory to reduce API calls
imputed = pd.read_csv("data/cache/imputed_zip.csv")
reverse_dict = dict(zip(imputed["LOCATION"], imputed["ZIP_CODE_IMPUTED"]))
coords = []
zips = []


# Helper function
def impute(coord):
    if not reverse_dict.get(coord):
        if reverse_geocode(coord):
            zip = reverse_geocode(coord).raw["address"].get("postcode")
            reverse_dict[coord] = zip
            coords.append(coord)
            zips.append(zip)
            pd.DataFrame({"LOCATION": coords, "ZIP_CODE_IMPUTED": zips}).to_csv(
                "data/cache/imputed_zip.csv", index=False
            )
            return zip
        else:
            return None
    else:
        print(f"{coord}:{reverse_dict[coord]} exists")
        return reverse_dict[coord]


df_null_zip["ZIP_CODE_IMPUTED"] = df_null_zip["LAT_LON"].progress_apply(impute)
# %%
# Drop duplicates
df_null_zip = ~df_null_zip[["LATITUDE", "LONGITUDE", "ZIP_CODE_IMPUTED"]].duplicated()
# Save lookup to csv
df_null_zip.to_csv("data/imputed_zip.csv", index=False)
