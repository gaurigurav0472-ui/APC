import numpy as np

# Create a NumPy array containing numbers from 1 to 20
A = np.arange(1, 21)

print("Original Array:")
print(A)

# Display first 5 elements
print("\nFirst 5 Elements:")
print(A[:5])

# Display last 5 elements
print("\nLast 5 Elements:")
print(A[-5:])

# Display alternate elements
print("\nAlternate Elements:")
print(A[::2])

# Display elements in reverse order
print("\nReverse Order:")
print(A[::-1])