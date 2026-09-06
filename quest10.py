import numpy as np

# Define matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
addition = A + B
print("\nMatrix Addition:")
print(addition)

# Matrix Subtraction
subtraction = A - B
print("\nMatrix Subtraction:")
print(subtraction)

# Matrix Multiplication
multiplication = np.dot(A, B)
print("\nMatrix Multiplication:")
print(multiplication)

# Transpose
transpose_A = A.T
print("\nTranspose of Matrix A:")
print(transpose_A)
