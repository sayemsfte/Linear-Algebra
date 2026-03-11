import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

cos_theta = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle = np.arccos(cos_theta)

print("Angle between vectors (radians):", angle)
