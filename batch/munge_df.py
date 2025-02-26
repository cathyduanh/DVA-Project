# %%
import pandas as pd
import numpy as np


def munge_df(df):
    """
    Returns a dataframe after uppercasing column names and merging
    weather station and imputed zipcodes.

    Parameters
    ----------
    df : DataFrame
        The NYC crash dataset

    Returns
    -------
    DataFrame
        With new columns `LATITUDE_WEATHER_STATION`, `LONGITUDE_WEATHER_STATION`,
        `DISTANCE_FROM_WEATHER_STATION`, and `ZIP_CODE_IMPUTED`.
    """
    # Replace column name spaces with underscore
    df.columns = df.columns.str.replace(" ", "_")

    df_nearest = pd.read_csv("data/weather_station_mapping.csv")

    df = df.merge(
        df_nearest,
        left_on=["LATITUDE", "LONGITUDE"],
        right_on=["LATITUDE_ACCIDENT", "LONGITUDE_ACCIDENT"],
        how="left",
        validate="m:1",
    )

    df_null_zip = pd.read_csv("data/imputed_zip.csv")

    df = df.merge(df_null_zip, on=["LATITUDE", "LONGITUDE"], how="left", validate="m:1")

    df["ZIP_CODE"] = np.where(
        df["ZIP_CODE"].isnull(), df["ZIP_CODE_IMPUTED"], df["ZIP_CODE"]
    )

    return df
