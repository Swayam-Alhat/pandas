import pandas as pd

df = pd.read_csv('./TMDB - movies.csv')

# Data Cleaning

# Convert budget & revenue column into integer/float datatype
df["budget"] = df["budget"].str.replace(',','').astype(float).astype(int)
# add astype(int) to remove decimal numbers
df["revenue"] = df["revenue"].str.replace(',','').astype(float).astype(int)

# create new column of year
df["year"] = df["movie"].str[-5:-1].astype(int)
# remove year value from movie name.
df["movie"] = df["movie"].str[0:-6]
# remove start & end white spaces from movie name
df["movie"] = df["movie"].str.strip()
# reorder the column position. place column "year" next to column "movie"
year_column = df.pop("year")
df.insert(1,"year",year_column)


# Data exploration
# print(df.isnull().sum()) 
# print(df.shape)
# print(df.dtypes)
# print(df.describe())

# Movie with highest budget
highest_budget = df["budget"].max()
high_budget_movie = df[df["budget"] == highest_budget]
# print(f"Movie with highest budget: {high_budget_movie.iat[0,0]}") # Pirates of the Caribbean: At World's End

# print(f"{"="*50}")

# Movie with Lowest budget
lowest_budget = df["budget"].min()
lowest_budget_movie = df[df["budget"] == lowest_budget]
# print(f"Movie with lowest budget: {lowest_budget_movie.iat[0,0]}")  # Shaun of the Dead

# print(f"{"="*50}")

# Movie with highest revenue
highest_revenue = df["revenue"].max()
highest_revenue_movie = df[df["revenue"] == highest_revenue]
# print(f"Movie with highest revenue:  \n {highest_revenue_movie}")

# print(f"{"="*50}")

# Movie with lowest revenue
lowest_revenue = df["revenue"].min()
lowest_revenue_movie = df[df["revenue"] == lowest_revenue]
# print(f"Movie with lowest revenue: \n {lowest_revenue_movie}")


# Data analysis
print(f"Movies which are in profit: \n {df[df['revenue'] - df['budget'] > 0]}")

