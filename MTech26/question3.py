import numpy as np

# Create a 3 × 3 array containing numbers from 1 to 9
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Find the shape
print("Shape:", arr.shape)

# Sum of all elements
print("Sum of all elements:", arr.sum())

# Sum of each row
print("Sum of each row:", arr.sum(axis=1))
