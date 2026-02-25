import pandas as pd

df = pd.read_csv('./TMDB - movies.csv')
print(df)
print(df.dtypes)
print(f"{"=" * 40}")

df["budget"] = df["budget"].str.replace(',','').astype(float)
df["revenue"] = df["revenue"].str.replace(',','').astype(float)
print(df.head())
print(df.dtypes)
