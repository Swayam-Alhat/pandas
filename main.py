import pandas as pd

df = pd.read_csv('./TMDB - movies.csv')
print(df.head())
print(f"{"=" * 40}")

df["movie"] = 0
print(df.head())


