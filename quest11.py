import numpy as np

# Define matrix
A = np.array([
    [2, 1, 3],
    [1, 0, 2],
    [3, 2, 1]
])

print("Matrix A:")
print(A)

# Calculate determinant
det = np.linalg.det(A)
print("\nDeterminant of Matrix:")
print(round(det, 2))

# Calculate inverse
if det != 0:
    inverse = np.linalg.inv(A)
    print("\nInverse of Matrix:")
    print(inverse)
else:
    print("\nInverse does not exist because determinant is zero.")

# Calculate rank
rank = np.linalg.matrix_rank(A)
print("\nRank of Matrix:")
print(rank)
