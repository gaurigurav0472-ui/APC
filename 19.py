import numpy as np

# Create a 3D array of shape (2, 3, 4)
arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

# Access the first element
print("\nFirst Element:")
print(arr[0, 0, 0])

# Access the last element
print("\nLast Element:")
print(arr[-1, -1, -1])

# Access element at index [0, 1, 2]
print("\nElement at index [0, 1, 2]:")
print(arr[0, 1, 2])

# Access element at index [1, 2, 3]
print("\nElement at index [1, 2, 3]:")
print(arr[1, 2, 3])