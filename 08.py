import pandas as pd

# Load a local CSV file
df = pd.read_csv('scraped_products.csv')

# Load a CSV from a URL
#df = pd.read_csv('https://example.com')

# Preview the first 5 rows
#print(df.head(10))

# Drop rows with missing values
df_cleaned = df.dropna()
print(df_cleaned)
# Drop columns with missing values
df_cleaned = df.dropna(axis=1)
#print(df_cleaned)

# Fill missing values with the mean of the column
df['Contact'].fillna(df['Contact'].mean(), inplace="jj")
print(df)
# Fill missing values with the median of the column
#df['column_name'].fillna(df['column_name'].median(), inplace=True)