import numpy as np

# Rotation matrix (90° around Z-axis)
Rz = np.array([
    [0, -1, 0],
    [1,  0, 0],
    [0,  0, 1]
])

# Scaling matrix (stretch X by 2)
S = np.diag([2, 1, 1])

# Original vector
v = np.array([1, 0, 0])

# Combine transformations: Apply rotation first, then scale
combined = S @ Rz
transformed = combined @ v

print("Transformed Vector:", transformed)
