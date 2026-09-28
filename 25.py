import numpy as np

# Create a random 3D array of shape (3, 4, 5)
arr = np.random.randint(1, 101, size=(3, 4, 5))

# Flatten the array
flat_arr = arr.flatten()

# Calculate average
average = np.mean(flat_arr)

# Display elements
greater_than_50 = flat_arr[flat_arr > 50]
even_numbers = flat_arr[flat_arr % 2 == 0]
less_than_average = flat_arr[flat_arr < average]

print("3D Array:")
print(arr)

print("\nFlattened Array:")
print(flat_arr)

print("\nElements Greater Than 50:")
print(greater_than_50)

print("\nEven Numbers:")
print(even_numbers)

print("\nAverage:", average)

print("\nElements Less Than Average:")
print(less_than_average)