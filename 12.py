import numpy as np

# Create an array of 10 integers
A = np.array([25, 60, 45, 80, 30, 55, 70, 40, 90, 15])

print("Original Array:")
print(A)

# Replace elements greater than 50 with 0
A[A > 50] = 0

print("\nArray after replacing elements greater than 50 with 0:")
print(A)