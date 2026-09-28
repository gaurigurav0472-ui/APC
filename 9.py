import numpy as np

# Create a 4 × 4 NumPy array
A = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("Original 4 × 4 Array:")
print(A)

# Display the first row
print("\nFirst Row:")
print(A[0, :])

# Display the last column
print("\nLast Column:")
print(A[:, -1])

# Display the diagonal elements
print("\nDiagonal Elements:")
print(np.diag(A))

# Display the second and third rows
print("\nSecond and Third Rows:")
print(A[1:3, :])