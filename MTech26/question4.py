import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Get the element "5"
print("Element 5:", arr[1, 1])

# Get the last column
print("Last column:", arr[:, -1])

# Get the second row
print("Second row:", arr[1, :])
