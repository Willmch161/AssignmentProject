import numpy as np

# Function to generate a random matrix
def generate_matrix(size, name):
    matrix = np.random.randint(1, 10, (size, size))  # Random numbers between 1 and 9
    print(f"\nMatrix {name}:\n", matrix)
    return matrix

# Define matrix size (square matrix)
size = 3  # Change this to any size you want

# Generate random matrices
A = generate_matrix(size, "A")
B = generate_matrix(size, "B")

# Matrix Operations
addition = A + B
subtraction = A - B
multiplication = np.dot(A, B)
transpose_A = np.transpose(A)
det_A = np.linalg.det(A)

# Handle inverse calculation
try:
    inverse_A = np.linalg.inv(A)
except np.linalg.LinAlgError:
    inverse_A = "Matrix A is singular, inverse does not exist."

# Display results
print("\nAddition:\n", addition)
print("\nSubtraction:\n", subtraction)
print("\nMultiplication:\n", multiplication)
print("\nTranspose of A:\n", transpose_A)
print("\nDeterminant of A:", round(det_A, 2))
print("\nInverse of A:\n", inverse_A)

  
  