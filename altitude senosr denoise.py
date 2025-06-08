import numpy as np
import matplotlib.pyplot as plt

# Simulated altitude data (ground truth)
true_altitude = np.sin(np.linspace(0, 2*np.pi, 100))

# Adding noise to simulate sensor error
noise = np.random.normal(0, 0.2, 100)
noisy_altitude = true_altitude + noise

# Construct matrix with repeated noisy signals (simulate multivariate time series)
data_matrix = np.vstack([noisy_altitude, noisy_altitude + np.random.normal(0, 0.05, 100)])

# Apply SVD
U, S, Vt = np.linalg.svd(data_matrix, full_matrices=False)

# Keep only the first singular value to filter noise
S_filtered = np.zeros_like(S)
S_filtered[0] = S[0]
denoised_matrix = U @ np.diag(S_filtered) @ Vt

# Plot
plt.plot(true_altitude, label='True')
plt.plot(noisy_altitude, label='Noisy')
plt.plot(denoised_matrix[0], label='Denoised (SVD)', linestyle='--')
plt.legend()
plt.title("SVD Denoising of Altitude Sensor")
plt.show()
