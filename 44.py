#Perform matrix multiplication

import numpy as np
matrix1 = np.array([[1, 2],
                   [3, 4]])
matrix2 = np.array([[5, 6],
                   [7, 8]])

result = np.dot(matrix1, matrix2)
print("Matrix Multiplication Result:")
print(result)
