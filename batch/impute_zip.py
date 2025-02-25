# %%
import pandas as pd
import numpy as np

# %%
###########################
# IMPORT DATA
###########################
df = pd.read_csv("data/Motor_Vehicle_Collisions_-_Crashes.csv")
df = df.head(20)
# Replace column name spaces with underscore
df.columns = df.columns.str.replace(" ", "_")
df_null_zip = pd.read_csv("data/imputed_zip.csv")

df = df.merge(df_null_zip, on=["LATITUDE", "LONGITUDE"], how="left", validate="m:1")

df["ZIP_CODE"] = np.where(
    df["ZIP_CODE"].isnull(), df["ZIP_CODE_IMPUTED"], df["ZIP_CODE"]
)
df
# %%
