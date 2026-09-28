import numpy as np

# Store marks of 10 students
marks = np.array([78, 85, 92, 67, 74, 88, 95, 81, 69, 90])

print("Marks of 10 Students:")
print(marks)

# Calculate statistics
highest = np.max(marks)
lowest = np.min(marks)
average = np.mean(marks)
median = np.median(marks)
standard_deviation = np.std(marks)

print("\nHighest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Median:", median)
print("Standard Deviation:", standard_deviation)