# Create a matrix and find its transpose.

import numpy as np

matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

transpose = np.transpose(matrix)
print("Original Matrix:")
print(matrix)
print("Transposed Matrix:")
print(transpose)

