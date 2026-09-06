import numpy as np

# Define matrix
A = np.array([
    [4, 1],
    [2, 3]
])

print("Matrix A:")
print(A)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
