# quantum_discord_example

This Python script uses the Qiskit library to calculate the quantum discord of a two-qubit quantum state. Quantum discord is a measure of quantum correlations between parts of a quantum system. Here's a step-by-step explanation:

Import necessary modules: The script begins by importing the necessary Python modules. numpy is a general-purpose array-processing package, while qiskit.quantum_info is a part of the Qiskit library that provides classes for quantum states and quantum channels.

Define the density matrix: The script defines a 4x4 matrix rho_matrix representing the density matrix of a two-qubit quantum state. A density matrix is a matrix that describes the statistical state of a quantum system.

Create a DensityMatrix object: The script then creates a DensityMatrix object rho from rho_matrix. This object can be used to calculate various properties of the quantum state.

Calculate the von Neumann entropy of the full state: The script calculates the von Neumann entropy of the full quantum state using the entropy function from Qiskit. The von Neumann entropy is a measure of the "mixedness" of a quantum state, with higher values indicating more mixed states.

Calculate the reduced density matrix: The script calculates the reduced density matrix for the first qubit (qubit 1) using the partial_trace function. The reduced density matrix describes the state of one part of a quantum system when we ignore the rest of the system.

Calculate the von Neumann entropy of the reduced density matrix: The script calculates the von Neumann entropy of the reduced density matrix.

Calculate the quantum discord: Finally, the script calculates the quantum discord of the state by subtracting the von Neumann entropy of the reduced density matrix from the von Neumann entropy of the full state. The quantum discord is a measure of the quantumness of the correlations in a quantum system. It is zero for classical states and greater than zero for non-classical states.

In summary, this script calculates the quantum discord of a two-qubit quantum state, which is a measure of the quantum correlations in the state.
