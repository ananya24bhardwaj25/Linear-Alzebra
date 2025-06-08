import numpy as np

A = np.array([[12, -51, 4],
              [6, 167, -68],
              [-4, 24, -41]])

Q, R = np.linalg.qr(A)

print("Q:\n", Q)
print("R:\n", R)
