# Check if two matrices are equal

import numpy as np

matrix1 = np.array([[1, 2],
                   [3, 4]])
matrix2 = np.array([[1, 2],
                   [3, 4]])

are_equal = np.array_equal(matrix1, matrix2)
print("Are the matrices equal?", are_equal)
