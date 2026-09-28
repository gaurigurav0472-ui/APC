import numpy as np

# Create a 3D array of shape (2, 3, 4)
arr = np.arange(1, 25).reshape(2, 3, 4)

# Display the array
print("3D Array:")
print(arr)

# Display dimensions, shape, and size
print("\nNumber of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)