import numpy as np

# Marks of 20 students
marks = np.array([
    65, 78, 82, 91, 56,
    74, 88, 95, 63, 71,
    84, 59, 76, 89, 68,
    92, 73, 81, 55, 87
])

# Calculate class average
average = np.mean(marks)

# Display marks above the average
above_average = marks[marks > average]

print("Marks of 20 Students:")
print(marks)

print("\nClass Average:", average)

print("\nStudents Scoring Above Average:")
print(above_average)