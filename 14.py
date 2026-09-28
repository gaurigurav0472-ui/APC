import numpy as np

# Create an array containing duplicate values
A = np.array([10, 20, 30, 20, 40, 10, 50, 30, 60, 20])

print("Original Array:")
print(A)

# Find unique elements
unique_elements = np.unique(A)

print("\nUnique Elements:")
print(unique_elements)