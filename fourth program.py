import pandas as pd
import numpy as np

# Convert Numpy array to DataFrame
numpy_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_from_numpy = pd.DataFrame(numpy_array, columns=['A', 'B', 'C'])

print("DataFrame from Numpy array:")
print(df_from_numpy)

# Convert Pandas Series to DataFrame
pandas_series = pd.Series([10, 20, 30, 40, 50], name='Numbers')
df_from_series = pd.DataFrame(pandas_series)

print("\nDataFrame from Pandas Series:")
print(df_from_series)

