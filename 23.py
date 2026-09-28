import numpy as np

# Create a 3D array of shape (2, 3, 4)
arr = np.arange(1, 25).reshape(2, 3, 4)

# Flatten the 3D array into a 1D array
flattened = arr.flatten()

print("Original 3D Array:")
print(arr)

print("\nFlattened 1D Array:")
print(flattened)