#Extract a submatrix from a larger matrix

import numpy as np
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

submatrix = matrix[1:, 1:]
print("Submatrix:")
print(submatrix)
