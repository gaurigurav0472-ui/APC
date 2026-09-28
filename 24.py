import numpy as np

# Create a 3D array containing integers from 1 to 27
arr = np.arange(1, 28).reshape(3, 3, 3)

# Flatten the 3D array
flat_arr = arr.flatten()

# Calculate statistics
total = np.sum(flat_arr)
average = np.mean(flat_arr)
maximum = np.max(flat_arr)
minimum = np.min(flat_arr)

print("Original 3D Array:")
print(arr)

print("\nFlattened 1D Array:")
print(flat_arr)

print("\nSum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)