import numpy as np

# Create a 4 × 4 matrix
A = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("4 × 4 Matrix:")
print(A)

# Calculate sum of each row
row_sum = np.sum(A, axis=1)

# Calculate sum of each column
column_sum = np.sum(A, axis=0)

print("\nSum of Each Row:")
print(row_sum)

print("\nSum of Each Column:")
print(column_sum)