import numpy as np

A = np.array([[3, 2, 2],
              [2, 3, -2]])

U, S, Vt = np.linalg.svd(A)

print("U:\n", U)
print("Singular Values:", S)
print("Vᵗ:\n", Vt)
