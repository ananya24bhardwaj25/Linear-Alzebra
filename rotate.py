import math
import numpy as np

def rotation_matrix_x(theta):
    """Roll - Rotation around X-axis"""
    rad = math.radians(theta)
    return np.array([
        [1, 0, 0],
        [0, math.cos(rad), -math.sin(rad)],
        [0, math.sin(rad), math.cos(rad)]
    ])

def rotation_matrix_y(theta):
    """Pitch - Rotation around Y-axis"""
    rad = math.radians(theta)
    return np.array([
        [math.cos(rad), 0, math.sin(rad)],
        [0, 1, 0],
        [-math.sin(rad), 0, math.cos(rad)]
    ])

def rotation_matrix_z(theta):
    """Yaw - Rotation around Z-axis"""
    rad = math.radians(theta)
    return np.array([
        [math.cos(rad), -math.sin(rad), 0],
        [math.sin(rad), math.cos(rad), 0],
        [0, 0, 1]
    ])
def rotate_vector(v, roll=0, pitch=0, yaw=0):
    Rx = rotation_matrix_x(roll)
    Ry = rotation_matrix_y(pitch)
    Rz = rotation_matrix_z(yaw)

    # Combined rotation matrix: R = Rz * Ry * Rx
    R = Rz @ Ry @ Rx
    return R @ v
# Original vector pointing forward
v = np.array([1, 0, 0])

# Rotate: yaw=90° (left turn), pitch=0, roll=0
rotated = rotate_vector(v, roll=0, pitch=0, yaw=90)
print("Rotated Vector (Yaw 90°):", rotated)

# Rotate: pitch=90° (nose up)
rotated2 = rotate_vector(v, roll=0, pitch=90, yaw=0)
print("Rotated Vector (Pitch 90°):", rotated2)

# Rotate: roll=90° (side tilt)
v2 = np.array([0, 1, 0])
rotated3 = rotate_vector(v2, roll=90, pitch=0, yaw=0)
print("Rotated Vector (Roll 90°):", rotated3)
