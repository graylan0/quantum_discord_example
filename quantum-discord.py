import numpy as np
from qiskit.quantum_info import DensityMatrix, entropy, partial_trace

# Define a two-qubit density matrix as a matrix
rho_matrix = np.array([[0.5, 0, 0, 0.5], [0, 0, 0, 0], [0, 0, 0, 0], [0.5, 0, 0, 0.5]])

# Create a density matrix object from the matrix representation
rho = DensityMatrix(rho_matrix)

# Calculate the von Neumann entropy of the full state
s_rho = entropy(rho, base=2)
print(f"Von Neumann entropy of rho: {s_rho}")

# Calculate the reduced density matrix for qubit 1
rho_X = partial_trace(rho, [1])

# Calculate the von Neumann entropy of the reduced density matrix
s_rho_X = entropy(rho_X, base=2)
print(f"Von Neumann entropy of rho_X: {s_rho_X}")

# Calculate the quantum discord of the state
D = s_rho - s_rho_X
print(f"Quantum discord of rho: {D}")
