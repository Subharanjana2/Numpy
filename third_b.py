import pandas as pd

# Reading data from a CSV file
df = pd.read_csv('data.csv')


# Display the first few rows of the DataFrame
print(df.head())

# Display information about the DataFrame
print(df.info())

# Summary statistics of the DataFrame
print(df.describe())


# Select a single column as a Series
column_series = df['Column_Name']

# Select multiple columns as a new DataFrame
new_df = df[['Column1', 'Column2']]

# Select rows based on conditions
filtered_df = df[df['Column_Name'] > 10]

# Select a single column as a Series
column_series = df['Column_Name']

# Select multiple columns as a new DataFrame
new_df = df[['Column1', 'Column2']]

# Select rows based on conditions
filtered_df = df[df['Column_Name'] > 10]

# Add a new column to the DataFrame
df['New_Column'] = [1, 2, 3, 4, 5]

# Remove a column from the DataFrame
df.drop('Column_Name', axis=1, inplace=True)

# Group data by a column and calculate aggregate statistics
grouped_df = df.groupby('Group_Column')['Numeric_Column'].mean()

# Multiple aggregate functions
grouped_df = df.groupby('Group_Column')['Numeric_Column'].agg(['mean', 'sum'])


# Check for missing values in the DataFrame
missing_values = df.isnull().sum()

# Drop rows with any missing values
df.dropna(inplace=True)

# Fill missing values with a specific value
df.fillna(0, inplace=True)

# Check for missing values in the DataFrame
missing_values = df.isnull().sum()

# Drop rows with any missing values
df.dropna(inplace=True)

# Fill missing values with a specific value
df.fillna(0, inplace=True)

