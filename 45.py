# Find the sum of the main diagonal elements of a matrix

import numpy as np
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

diagonal_sum = np.trace(matrix)
print("Sum of Main Diagonal Elements:", diagonal_sum)
