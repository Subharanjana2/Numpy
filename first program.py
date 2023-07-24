import numpy as np

# Creating a 1-dimensional array
arr1d = np.array([1, 2, 3, 4, 5])

# Creating a 2-dimensional array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
result_add = a + b  # Output: [5, 7, 9]

# Element-wise subtraction
result_subtract = a - b  # Output: [-3, -3, -3]

# Element-wise multiplication
result_multiply = a * b  # Output: [4, 10, 18]

# Element-wise division
result_divide = a / b  # Output: [0.25, 0.4, 0.5]


matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix multiplication using dot function
result_matrix_mult = np.dot(matrix_a, matrix_b)
# Output: [[19, 22],
#          [43, 50]]

arr = np.array([1, 2, 3, 4, 5])

# Sum of all elements in the array
sum_of_elements = np.sum(arr)  # Output: 15

# Minimum and maximum value in the array
min_value = np.min(arr)  # Output: 1
max_value = np.max(arr)  # Output: 5

# Mean and standard deviation of the array
mean_value = np.mean(arr)  # Output: 3.0
std_deviation = np.std(arr)  # Output: 1.4142135623730951


arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array into a 2x3 matrix
reshaped_arr = arr.reshape(2, 3)
# Output: [[1, 2, 3],
#          [4, 5, 6]]
