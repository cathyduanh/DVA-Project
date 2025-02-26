# %%
from batch.munge_df import munge_df

import pandas as pd

df = pd.read_csv("data/Motor_Vehicle_Collisions_-_Crashes.csv")

df = munge_df(df)
df = df[~df["LOCATION"].isnull()].head(20)

df.to_csv("test.csv", index=False)
# %%
