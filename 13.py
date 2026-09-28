import numpy as np

# Create an unsorted NumPy array
A = np.array([45, 12, 78, 23, 56, 9, 34, 67])

print("Original Array:")
print(A)

# Display in ascending order
ascending = np.sort(A)

# Display in descending order
descending = np.sort(A)[::-1]

print("\nAscending Order:")
print(ascending)

print("\nDescending Order:")
print(descending)