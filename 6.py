import numpy as np

# Create two 3 × 3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Perform matrix addition
C = A + B

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Addition (A + B):")
print(C)