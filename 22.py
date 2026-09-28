import numpy as np

# Generate a random 3D array of shape (3, 4, 5)
arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Random 3D Array:")
print(arr)

# Calculate statistical measures
mean = np.mean(arr)
median = np.median(arr)
standard_deviation = np.std(arr)
variance = np.var(arr)
minimum = np.min(arr)
maximum = np.max(arr)

print("\nMean:", mean)
print("Median:", median)
print("Standard Deviation:", standard_deviation)
print("Variance:", variance)
print("Minimum:", minimum)
print("Maximum:", maximum)