#Find the determinant of a square matrix

import numpy as np
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

determinant = np.linalg.det(matrix)
print("Determinant of the Matrix:", determinant)

