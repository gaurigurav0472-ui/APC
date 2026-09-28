import numpy as np

# Create two NumPy arrays
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Array A:")
print(A)

print("\nArray B:")
print(B)

# Horizontal concatenation
horizontal = np.hstack((A, B))

# Vertical concatenation
vertical = np.vstack((A, B))

print("\nHorizontal Concatenation:")
print(horizontal)

print("\nVertical Concatenation:")
print(vertical)